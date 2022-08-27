from twilio.rest import Client
import logging

LOG_FILENAME = 'Logfiles/twilioMain.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format='%(asctime)s, %(levelname)s, %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class TWilio:
	def __init__(self,sid,from_num,authToken,):
		self.account_sid = sid
		self.auth_token  = authToken
		self.from_num = from_num
	def connect(self):
		try:		
			self.client = Client(self.account_sid, self.auth_token)
		except Exception as e:
			logging.error("The connect error %s,%s"%(e,type(e)))
				
	def send(self,to,message):
		try:
			msg = client.messages.create(to=to, from_=self.from_num,body=message)
			return msg
		except Exception as e:
			logging.error("The send error %s,%s"%(e,type(e)))	
		