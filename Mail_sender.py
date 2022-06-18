from email.mime.text import MIMEText
import smtplib

SMTP_URL = 'smtp.office365.com'
SMTP_PORT = 587
SMTP_USER = ''
SMTP_PASS = ''


class Mail_sender:

    def __init__(self):
        pass

    def send_email(self,email_to, email_subject, data):
        msg = MIMEText(data, 'html')
        msg['Subject'] = email_subject
        msg['To'] = email_to
        msg['From'] = SMTP_USER
        mail = smtplib.SMTP(SMTP_URL, SMTP_PORT)
        mail.starttls()
        mail.login(SMTP_USER, SMTP_PASS)
        mail.sendmail(SMTP_USER, email_to, msg.as_string())
        mail.quit()
