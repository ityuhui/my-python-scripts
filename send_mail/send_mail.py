#! /usr/bin/env python3
#coding: utf-8
# 这个脚本在163上不好用，163可能不允许25端口连接

import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = sys.argv[1]
receiver = sys.argv[3]
subject = 'mail title'
smtpserver = 'smtp.163.com'
username = sys.argv[3]
password = sys.argv[4]
print password

msg = MIMEText('hello,mail body','text','utf-8')
msg['Subject']=Header(subject,'utf-8')
smtp = smtplib.SMTP(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
