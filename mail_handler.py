import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mail_template import create_email
from constants import MAIL_SMTP_SERVER, MAIL_SMTP_PORT, MAIL_LOGIN, MAIL_PASSWORD

class EmailSender:
  def __init__(self, sender_email, receiver_email):
    self.sender_name = "LeetCode Team"
    self.sender_email = sender_email
    self.receiver_email = receiver_email
    self.login = MAIL_LOGIN
    self.password = MAIL_PASSWORD
    self.smtp_server = MAIL_SMTP_SERVER
    self.port = MAIL_SMTP_PORT

  def create_message(self, subject, html):
    message = MIMEMultipart()
    message["From"] = f"{self.sender_name} <{self.sender_email}>"
    message["To"] = self.receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(html, "html"))
    return message

  def send_email(self, message):
    with smtplib.SMTP(self.smtp_server, self.port) as server:
      server.starttls()  # Secure the connection
      server.login(self.login, self.password)
      server.sendmail(self.sender_email, self.receiver_email, message.as_string())
    print("Email sent successfully")
