#! /usr/bin/env python3
#coding: utf-8
# 可以用于在公司内部，邮件发送服务器不需要验证

import sys
import smtplib

sender = sys.argv[1]
receiver = sender
smtpserver = sys.argv[2]

msg = "\r\n".join([
  "From: %s" % sender,
  "To: %s" % receiver,
  "Subject: Just a message",
  "",
  "Why, oh why"
])


smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpserver)
smtp.sendmail(sender,receiver,msg)
smtp.quit()
