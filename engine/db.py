__author__ = 'Nick'

import MySQLdb

db = MySQLdb.connect(host='localhost',
					user='root',
					passwd='root',
					db='PySearch')


def cursor():
	return db.cursor()