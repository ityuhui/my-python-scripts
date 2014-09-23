import os


def parseComflex(full_str):
	nv = {}
	position = full_str.rfind('-')
	name = full_str[:position]
	ver = full_str[position+1:]
	nv[name]=ver
	return nv


def parseLibStr(full_str):
	nv = {};
	if(full_str.count('.')>0):
		nv = parseComflex(full_str)
	else:
		nv[full_str] = "no version" 
	return nv


def printList(alist,fh):
	for item in alist:
		for (d,x) in item.items():
			print >>fh,x




file_object = open('temp.txt','r')
#fwo = open('bn.csv','w');
try:
	d = {}
	for line in file_object:
		dn = os.path.dirname(line)
		d[dn]=1
		#bn = os.path.basename(line)
		#elem = parseLibStr(bn[:-5])
		#d.append(elem)
		#print dn
#	printList(d,fwo)
	print d
	print len(d)
		
finally:
	file_object.close()
#	fwo.close()


