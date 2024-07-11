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