
insert_impression = "insert into impressions (timestamp,product_id,location,device) values ('%s','%s','%s','%s')"
insert_transaction = "insert into transactions (timestamp,product_id,location,device) values ('%s','%s','%s','%s')"

city_dict = {'Hull':{'population':284321},
'Belfast':{'population':280211},
'Stoke':{'population':270726},
'Newcastle':{'population':268064},
'Wolverhampton':{'population':265178},
'Derby':{'population':255394},
'Southampton':{'population':253651},
'Portsmouth':{'population':238137},
'Plymouth':{'population':234982},
'Bradford':{'population':349561},
'Cardiff':{'population':335145},
'Coventry':{'population':325949},
'Nottingham':{'population':289301},
'Edinburgh':{'population':459366},
'Leicester':{'population':443760},
'Birmingham':{'population':1085810},
'Glasgow':{'population':590507},
'Liverpool':{'population':552267},
'Bristol':{'population':535907},
'Sheffield':{'population':518090},
'Manchester':{'population':510746},
'Leeds':{'population':474632},
'Brighton and Hove':{'population':229700},
'London':{'population':8173941},
'Westminster':{'population':218791},
'Reading':{'population':218705},
'Northampton':{'population':215173},
'Luton':{'population':211228},
'Aberdeen':{'population':195021},
'Bolton':{'population':194189},
'Bournemouth':{'population':187503},
'Norwich':{'population':186682},
'Swindon':{'population':182441},
'Swansea':{'population':179485},
'Southend':{'population':175547},
'Middlesbrough':{'population':174700},
'Sunderland':{'population':174286},
'Milton Keynes':{'population':171750},
'Warrington':{'population':165456},
'Huddersfield':{'population':162949},
'Peterborough':{'population':161707},
'Oxford':{'population':159994},
'Slough':{'population':155298},
'Poole':{'population':154718},
'York':{'population':152841},
'Blackpool':{'population':147663},
'Dundee':{'population':147285},
'Cambridge':{'population':145818},
'Ipswich':{'population':144957}}


product_dict = {1:{'name':'The Fundamental','price':5}
				,2:{'name':'The Ewing','price':10}
				,3:{'name':'The Cousy','price':15}
				,4:{'name':'The Barkley','price':14}
				,5:{'name':'The Hakeem','price':13}
				,6:{'name':'The Irving','price':20}
				,7:{'name':'The Dipper','price':19}
				,8:{'name':'The Russell','price':18}
				,9:{'name':'The Mailman','price':6}
				,10:{'name':'The Mamba','price':8}}


device_lst = ['iPhone','Android Phone','iPad','Android Tablet','PC']


import numpy as np
import random
import getopt
import sys
import datetime


def random_num(mu,sigma,max_range,min_range):
	a = np.random.normal(mu,sigma)
	if a <= min_range:
		return min_range
	if a >= max_range:
		return max_range
	else:
		return int(a)

city_lst = [x for x in city_dict]
product_lst = [x for x in product_dict]

def rand_city(city_lst):
	return city_lst[random_num(30,10,48,0)]

def rand_product(product_lst):
	return product_lst[random_num(5,3,9,0)]

def rand_device(device_lst):
	return device_lst[random.randint(0,2)]


def gen_impression(db):
	impression = (str(datetime.datetime.now())
						,rand_product(product_lst)
						,rand_city(city_lst)
						,rand_device(device_lst))
	db.query(insert_impression % impression)
	return impression

def gen_transaction(db):
	transaction = (str(datetime.datetime.now())
						,rand_product(product_lst)
						,rand_city(city_lst)
						,rand_device(device_lst))
	db.query(insert_transaction % transaction)
	return impression


import _mysql
db = _mysql.connect(host='localhost',user='logger',db='webdata')
def table_inits(db):
	impressions_table_query = """CREATE table impressions(
			impression_id int NOT NULL AUTO_INCREMENT PRIMARY KEY
			,timestamp datetime
			,product_id int
			,location varchar(100)
			,device varchar(100))"""
	
	transactions_table_query = """CREATE table transactions(
		transaction_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
		timestamp datetime,
		product_id integer,
		location varchar(100),
		device varchar(100))"""


	try:
		db.query(impressions_table_query)
	except _mysql.OperationalError:
		print 'Impressions table already exists'

	try:
		db.query(transactions_table_query)
	except _mysql.OperationalError:
		print 'Transactions table already exists'		

	
def dropper(db):
	lst = ["impressions","transactions"]
	for table in lst:
		try:
			 db.query("drop table %s" % (table))
		except _mysql.OperationalError:
			print 'Unable to drop %s' % (table)