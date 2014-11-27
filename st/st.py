#! env python

import urllib2
import time
import sys



def onea(rate,ChengBen,hold):
	ChengBens = ChengBen * hold
	top = ChengBen * (1.0 + rate)
	tos = top * hold
	ear = tos - ChengBens
	print "%.2f" % top,"%.2f" % ear,rate*100
	sys.stdout.flush()

def maxmin(pri,ChengBen,hold):
	print pri,(pri - ChengBen )* hold, "%.2f%%" % ((pri / ChengBen - 1)*100) 
	sys.stdout.flush()
	
yhold = 9000
yChengBen = 1.671
yURL='http://hq.sinajs.cn/list=sh510050'

#onea(0.05,yChengBen,yhold)
#onea(0.1,yChengBen,yhold)
#onea(0.2,yChengBen,yhold)

req = urllib2.Request(yURL)
response = urllib2.urlopen(req)
the_page = response.read()
usarr = the_page.split(',')

maxmin(float(usarr[5]),yChengBen,yhold)
maxmin(float(usarr[4]),yChengBen,yhold)

while True:
	response = urllib2.urlopen(req)
	the_page = response.read()
	usarr = the_page.split(',')
	unowa = float(usarr[3])
	shouyi = ( unowa - yChengBen ) * yhold
	rat = ( unowa - yChengBen ) / yChengBen * 100.0 
	print unowa, shouyi, "%.2f%%" % rat
	sys.stdout.flush()
	time.sleep(60)
	

