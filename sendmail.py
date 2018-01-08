import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'haohe@ect888.com'
smtpserver = 'mail.ect888.com'
username = 'haohe'
password = 'haohe1989'

def send(receiver, subject, content):
	msg = MIMEText(content,'plain','utf-8')
	msg['Subject'] = Header(subject,'utf-8')

	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.set_debuglevel(True)
	smtp.login(username,password)
	smtp.sendmail(sender,receiver,msg.as_string())
	smtp.quit()

send('137044930@qq.com','test from local','hello world')