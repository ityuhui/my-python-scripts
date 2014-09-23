import os


def isFileExist(filename):
	if os.path.exists(filename):
		return True
	else:
		print filename,"does not exist"
		return False

try:
	fhr = open('update_name_ver.txt','r')
	fhw = open('source.txt','w')
	str_pre = "/pcc/lsfqa-trusted/blue/3rdparty/"
	count_for_not = 0
	for line in fhr:
		oj = line.split()
		name = oj[0]
		ver = oj[1]
		str_full = str_pre + name + "/" + ver + "/" + name + "-" + ver + ".jar"
		print >>fhw,str_full
		if not isFileExist(str_full):
			count_for_not += 1
	
	print "There are ",count_for_not," files not existing."
finally:
	fhr.close()
	fhw.close()


