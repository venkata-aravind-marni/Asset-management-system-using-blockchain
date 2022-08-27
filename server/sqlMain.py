import MySQLdb
import logging

LOG_FILENAME = 'Logfiles/sqlMain.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format='%(asctime)s, %(levelname)s, %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class MYsqldb:

	def __init__(self,host,user,password,database,tablename):
		self.host = host
		self.user = user
		self.password = password
		self.database = database 
		self.tablename = tablename

	def connect(self):
		try:
			self.db = MySQLdb.connect(sql_hostName,user,password,Database)
			self.cursor = db.cursor()	
		except Exception as e:
			logging.error("The connect error %s,%s"%(e,type(e)))

	def update(self):
		try:
			sql = "UPDATE "+self.tableName+" SET xxxxx = "+str()+" WHERE xxxx = "++" AND DataTime = "+"'"+str()+"'"		
			cursor.execute(sql)
			db.commit()
		except Exception as e:
			logging.error("The update error %s,%s"%(e,type(e)))	
			self.db.rollback()


	
	def insert(self):
		try:
		   sql = "INSERT INTO "+self.tableName+"(xxx,xxxx,xxxx) VALUES (default,"+"'"+"xxxx"+"'"+","+"'"+"xxxx"+"'"+",xxx,now())"			
		   cursor.execute(sql)
		   db.commit()
		except Exception as e:
			logging.error("The insert error %s,%s"%(e,type(e)))	
			self.db.rollback()
			   


	def get(self):
		try:
			sql = "SELECT * FROM "+self.tableName+" WHERE xxx ="+"xxxx"+" and DataTime = "+"'"+str()+"'"+""
			cursor.execute(sql)
			results = cursor.fetchall()
			if len(results) > 0:
				for row in results:				
					message.update({"xxxx":row[0]})
		except Exception as e:
			logging.error("The get error %s,%s"%(e,type(e)))	
			self.db.rollback()
					
	def delete(self):
		pass				
			

