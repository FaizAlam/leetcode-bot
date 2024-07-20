from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from database import mysql
from backend_main import initialise_cron
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from utils import SubscriptionUtils


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12720934'
app.config['MYSQL_PASSWORD'] = 'LunjcLNweD'
app.config['MYSQL_DB'] = 'sql12720934'
app.config['MYSQL_PORT'] = 3306

mysql.init_app(app)
scheduler = BackgroundScheduler()



def run_cron_for_streak_mails():
    initialise_cron()

# Schedule the cron job to run every day at 9:30 AM
scheduler.add_job(
    func=run_cron_for_streak_mails,
    trigger=CronTrigger(hour=11, minute=59),
)
scheduler.start()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

def validate_data(**kwargs):
    pass


@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        cur = mysql.connection.cursor()
        user_name = request.json['user_name']
        lc_user = request.json['lc_user']
        email = request.json['email']
        print("data received", request.json)
        #validate the received data
        print(user_name, lc_user, email)
        validate_data(user_name=user_name, lc_user=lc_user, email=email)
        cur.execute('''SELECT * FROM users WHERE lc_user=%s or email=%s''',(lc_user,email))
        data = cur.fetchall()
        if data:
            return jsonify({'message': 'user email mapping already exist!', 'status': 400})

        #insert the data into the database
        cur.execute('''INSERT INTO `users` (`lc_user`, `email`, `user_name`) VALUES (%s, %s, %s);''',(lc_user, email, user_name))
        mysql.connection.commit()
        cur.close()
        # send confirmation mail to user
        SubscriptionUtils.send_subs_mail(email)
        return jsonify({'message': 'Data added successfully', 'status': 200})

    except Exception as e:
        print("error in submitting user data", e, locals())
        return jsonify({'message': f'Some error occured {e}', 'status': 500})
    

@app.route('/delete', methods=['POST'])
def delete_data():
    try:
        cur = mysql.connection.cursor()
        email = request.json['email']
        cur.execute('''DELETE FROM users WHERE email=%s''',(email,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Data deleted successfully', 'status': 200})
    except Exception as e:
        print("error in deleting user data", e)
        return jsonify({'message': 'Some error occured', 'status': 500})

 
    
# @app.route('/claim', methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)

