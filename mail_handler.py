import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from constants import SENDER_EMAIL

class EmailSender:
  def __init__(self, receiver_email):
    self.sender_name = "RemindCode Team"
    self.sender_email = SENDER_EMAIL
    self.receiver_email = receiver_email
    # self.login = MAIL_LOGIN
    self.login = self.sender_email
    self.password = "kbevhpxqsypkdkbx"
    # self.smtp_server = MAIL_SMTP_SERVER
    self.smtp_server = "smtp.gmail.com"
    # self.port = MAIL_SMTP_PORT
    self.port = 465

  def create_message(self, subject, html):
    message = MIMEMultipart()
    message["From"] = f"{self.sender_name} <{self.sender_email}>"
    message["To"] = self.receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(html, "html"))
    return message

  def send_email(self, message):
    with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:
      # server.starttls()  # Secure the connection
      server.login(self.sender_email, self.password)
      server.sendmail(self.sender_email, self.receiver_email, message.as_string())
    print("Email sent successfully")
