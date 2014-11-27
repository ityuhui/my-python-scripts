import urllib2
import time
import sys



def onea(rate,cb,hold):
	cbs = cb * hold
	top = cb * (1.0 + rate)
	tos = top * hold
	ear = tos - cbs
	print "%.2f" % top,"%.2f" % ear,rate*100
	sys.stdout.flush()

def maxmin(pri,cb,hold):
	print pri,(pri - cb )* hold, "%.2f" % ((pri / cb - 1)*100) 
	sys.stdout.flush()
	
yhold = 500
ycb = 12.84

onea(0.05,ycb,yhold)
onea(0.1,ycb,yhold)
onea(0.2,ycb,yhold)

req = urllib2.Request('http://hq.sinajs.cn/list=sz000063')
response = urllib2.urlopen(req)
the_page = response.read()
usarr = the_page.split(',')

maxmin(float(usarr[5]),ycb,yhold)
maxmin(float(usarr[4]),ycb,yhold)

while True:
	response = urllib2.urlopen(req)
	the_page = response.read()
	usarr = the_page.split(',')
	unowa = float(usarr[3])
	shouyi = ( unowa - ycb ) * yhold
	rat = ( unowa - ycb ) / ycb * 100.0 
	print unowa, shouyi, "%.2f" % rat
	sys.stdout.flush()
	time.sleep(60)
	

