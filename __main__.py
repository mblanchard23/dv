from generator import *

try:
	opts,args = getopt.getopt(sys.argv[1:],'i:',['table='])
except getopt.GetoptError:
	print 'Parameter not recognised'
	sys.exit(2)

for opt, arg in opts:
	if opt == '-i':
		#Execute Inserts
		pass