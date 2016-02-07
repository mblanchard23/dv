from generator import *


import time
import random

def gen_loop_imp():
	a = True
	while a: 
		sleep_time = random.random()
		#print "Sleeping for %d" % (sleep_time)
		time.sleep(sleep_time) 
		print str(gen_impression(db)) + ' -- Impression'


def gen_loop_trans():
	b = True
	while b: 
		sleep_time = random.randint(1,5)
		#print "Sleeping for %d" % (sleep_time)
		time.sleep(sleep_time)
		print str(gen_transaction(db)) + ' -- Transaction'


# def query_db(db,q):
# 	db.query(q)
# 	res = db.store_result()
# 	return res.fetch_row(0) # returns all


try:
	opts,args = getopt.getopt(sys.argv[1:],'i')
except getopt.GetoptError:
	print 'Parameter not recognised'
	sys.exit(2)

for opt, arg in opts:
	if opt == '-i':
		import threading
		t_imp = threading.Thread(name='Impressions Generator',target=gen_loop_imp)
		t_trans = threading.Thread(name = 'Transactions Generator',target=gen_loop_trans)

		t_imp.start()
		t_trans.start()
