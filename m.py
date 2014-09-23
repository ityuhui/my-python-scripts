def printList(alist):
	for item in alist:
		print item
		
		
def removeDup(list1):
	lt = []
	for i in list1:
		if not i in lt:
			lt.append(i)
			print >>fw,i[1]
	printList(lt)




def handle_pa(pastr):
	blist = pastr.split('/')
	return blist[0:2]


fh = open('a.mak','r')
fw = open('b.txt','w')

try:
	alist = []
	allList = []
	for line in fh:
		alist = line.split()
		allList.append(handle_pa(alist[1][22:]))
	removeDup(allList)
	
finally:
	fh.close()
	fw.close()