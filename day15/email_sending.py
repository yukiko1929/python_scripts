from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_email(msg, subject, sender, receivers, host, passwd):
    message =  MIMEText(msg,'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(sender,passwd)
    smtp.sendmail(sender, receivers,message.as_string())

if __name__ == '__main__':
    msg = 'hello yukiko, would you like a cup of coffee?\r\n'
    subject = 'yuki\'s email'
    sender = 'zhangyuke199200@163.com'
    receivers = ['zhangyuke199200@163.com']
    host = 'smtp.163.com'
    passwd = getpass.getpass()
    send_email(msg,subject,sender,receivers,host, passwd)

