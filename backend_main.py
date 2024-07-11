from utils import ProcessData, ReminderUtilClass
from mail_handler import EmailSender
from mail_template import create_email
from mysql import connector
from mysql.connector import errorcode


def connect_to_db():
    config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'leetcode_notifier',
    'raise_on_warnings': True
    }
    try:
        cnx = connector.connect(**config)
        
        return cnx
    except connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None



def main(lc_user, user_mail, profile_name):
    process = ProcessData(lc_user)
    submissions = process.get_submissions_data()
    # print(submissions)
    if profile_name is None:
        profile_name = process.get_profile_data()
        print(profile_name)
    # diff = ReminderUtilClass(submissions).calculate_streak()
    # print(diff)
    # Usage
    ReminderUtilClass(submissions, profile_name, user_mail).send_streak_reminder()
    

    



    '''
    flow:
    take username, email as input
    put it in db
    
    at the time of running cron:
    pull up all the username,email from db
    process it one by one
    we will have username, email
    get the submissions for the user
    calculate the streak
    if streak present, send email to mantain streak
    else, send email to start streak

    
    '''



if __name__ == '__main__':
    # main()
    cnx = connect_to_db()
    if cnx is None:
        raise Exception("DB connection failed")
    cursor = cnx.cursor()
    query = ("SELECT * FROM users")
    cursor.execute(query)
    users_data = cursor.fetchall()
    cursor.close()
    cnx.close()
    for user in users_data:
        lc_user = user[1]
        user_mail = user[2]
        profile_name = user[3]
        main(lc_user, user_mail, profile_name)