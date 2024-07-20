from string import Template

def create_email(name, streak_length, leetcode_username):
    html_template = Template("""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Keep up the Streak!</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #f4f4f4;
          padding: 20px;
        }
        .container {
          max-width: 600px;
          margin: 0 auto;
          background-color: #fff;
          padding: 30px;
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
          color: #333;
          text-align: center;
        }
        p {
          color: #666;
          font-size: 16px;
          line-height: 1.6;
        }
        .button {
          display: inline-block;
          background-color: #4CAF50;
          color: white !important;
          padding: 10px 20px;
          text-align: center;
          text-decoration: none;
          border-radius: 5px;
          margin-top: 20px;
          font-weight: bold;
        }
        .button:hover {
          background-color: #45a049;
        }

      </style>
    </head>
    <body>
      <div class="container">
        <h1>Keep up the Streak, $Name!</h1>
        <p>Hi $Name,</p>
        <p>We noticed that you've been doing great on LeetCode! Your current streak is $StreakLength days. Keep up the excellent work!</p>
        <p>Challenge yourself to keep the streak going and continue your progress. Consistency is key to success!</p>
        <a href="https://leetcode.com/problemset/" class="button">Continue the Streak</a>
        <p>If you have any questions or need assistance, feel free to reach out to us. We're here to help!</p>
        <p>Best regards,</p>
        <p>Your LeetCode Team</p>
      </div>
    </body>
    </html>
    """)

    html = html_template.substitute(Name=name, StreakLength=streak_length, LeetCodeUsername=leetcode_username)
    return html

def subscription_mail():
    html_content = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to RemindCode</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            .container {
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
                text-align: center;
                padding-bottom: 20px;
                border-bottom: 1px solid #dddddd;
            }
            .header h1 {
                margin: 0;
                font-size: 24px;
                color: #333333;
            }
            .content {
                padding: 20px 0;
            }
            .content p {
                margin: 0;
                font-size: 16px;
                color: #555555;
                line-height: 1.5;
            }
            .button {
                display: block;
                width: fit-content;
                margin: 20px auto;
                padding: 10px 20px;
                background-color: #007bff;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
            }
            .footer {
                text-align: center;
                padding-top: 20px;
                border-top: 1px solid #dddddd;
                font-size: 14px;
                color: #888888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Welcome to RemindCode!</h1>
            </div>
            <div class="content">
                <p>Hi there,</p>
                <p>Thank you for subscribing to RemindCode. We're excited to have you on board!</p>
                <p>RemindCode is dedicated to helping you keep track of your coding progress and stay on top of your learning goals. We're here to remind you of your achievements and encourage you to keep pushing forward.</p>
                <p>If you have any questions or need assistance, feel free to reply to this email.</p>
                <p>Happy coding!</p>
                <p>The RemindCode Team</p>
            </div>
            <div class="footer">
                <p>© 2024 RemindCode. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>"""
  
    return html_content
