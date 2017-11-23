import json
import MySQLdb
import os

class dataDumper:
		"""This class dumps data into a SQL DB from the desired file."""

		def __init__(self):
			# Initialization
			self.db = ""
			self.sqlHost = os.environ['HOST']
			self.sqlUser = os.environ['USER']
			self.sqlPass = os.environ['PASS']
			self.datafile = './data/products.json'
			
			self.sqlDatabase = "Products"
			self.sqlTable = "Products"
			self.sqlColumn = "Name"

		def initConnection(self):
			try:
				self.db = MySQLdb.connect(host=self.sqlHost, user=self.sqlUser, passwd=self.sqlPass, db=self.sqlDatabase)
				cur = self.db.cursor()
				cur.execute("SELECT VERSION()")
				results = cur.fetchone()
				# Check if anything at all is returned
				if results:
					print(results)
					return True
				else:
					print("Things were not returned")
					return False               
			except MySQLdb.Error:
				print("ERROR IN CONNECTION")
				return False

		def dumpData(self):
			cur = self.db.cursor()
			Names = []
			data = json.load(open(self.datafile))
			for product in data:
				sql = 'INSERT INTO ' + self.sqlTable + ' (' + self.sqlColumn + ") VALUES ('" + product["name"] + "');"
				try:
					cur.execute(sql)
					self.db.commit()
					print("Committed " + product['name'] + " into DB.")
				except:
					self.db.rollback()
					print("**Failed** to commit " + product['name'] + " into DB.")
			cur.close()

if __name__ == '__main__':
    """ This is our main thread of execution, it starts all the work!"""

    dumper = dataDumper()
    dumper.initConnection()
    dumper.dumpData()
