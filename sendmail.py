import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '<your_email_address>'
smtpserver = '<smtp_server_address>'
username = '<user>'
password = '<passwd>'

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
