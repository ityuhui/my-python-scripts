fr = open('jar_list.txt','r')
fw = open('todo.sh','w')
try:
	str_pre = "cp ${PERF_3RDPARTY_LIBS}/"
	for line in fr:
		oj = line.split(',')
		target = oj[0]
		name =   oj[1]
		ver  = oj[2][:-1]

		str_2 = name + "/" + ver + "/" + name + "-" + ver + ".jar " + target
		
		str_all = str_pre + str_2
		print >>fw,str_all
finally:
	fr.close()
	fw.close()
