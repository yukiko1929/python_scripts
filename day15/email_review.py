import smtplib
import getpass
from email.mime.text import MIMEText
from email.header import Header

def send_email(message, sender, receiver, subject, host,passwd):
    message = MIMEText(message, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receiver[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(sender,passwd)
    smtp.sendmail(sender,receiver,message.as_string())
    # smtp.send(message)
    # smtp.close()

if __name__ == '__main__':
    message = 'for test'
    sender = 'zhangyuke199200@163.com'
    receiver = ['zhangyuke199200@163.com']
    subject = 'python smtplib test'
    host = 'smtp.163.com'
    passwd = getpass.getpass()
    send_email(message,sender,receiver,subject,host,passwd)
