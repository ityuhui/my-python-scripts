#! /usr/bin/env python3
#coding: utf-8

import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = 'uxr998@163.com'
receiver = 'uxr998@163.com'
subject = 'mail title'
smtpserver = 'smtp.163.com'
username = 'uxr998'
password = sys.argv[1]
print password

msg = MIMEText('hello,mail body','text','utf-8')
msg['Subject']=Header(subject,'utf-8')
smtp = smtplib.SMTP(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
