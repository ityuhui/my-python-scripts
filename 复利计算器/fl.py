import sys
a = {'base':float(sys.argv[1]),'rate':float(sys.argv[2]),'year':int(sys.argv[3])}
amount = ( 1.0 + a['rate']) ** a['year'] * a['base']
print amount
	