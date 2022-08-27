import ast
import paho.mqtt.client as mqtt
import logging



LOG_FILENAME = 'LogFiles/mqttMain.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format='%(asctime)s, %(levelname)s, %(message)s', datefmt='%Y-%m-%d %H:%M:%S')



class MQtt:
	def __init__(self,host,port,subTopic,timealive=60):
		self.host = host
		self.port = port
		self.timealive = timealive
		self.payload = None
		self.subTopic = subTopic

	def __on_connect(self,client, userdata, flags, rc):
		try:
			print "Connected with result code "+str(rc)
			if self.subTopic!=None:
				(result,mid)= client.subscribe(self.subTopic)
				print result
		except Exception as e:
			logging.error("The on_connect error %s,%s"%(e,type(e)))

	def __on_message(self,client, userdata, msg):
		try:			
		    data = msg.payload
		    message = ast.literal_eval(data)
		    self.payload = message
		    print self.payload
		except Exception as e:
			logging.error("The on_message error %s,%s"%(e,type(e)))	 	


	def connect(self):
		try:
			self.mqttc = mqtt.Client()
			self.mqttc.on_connect = self.__on_connect
			self.mqttc.on_message = self.__on_message
			self.mqttc.connect(self.host,self.port,self.timealive)
			
			if self.subTopic != None:
				print "Hu"				
				self.mqttc.loop_start()
				self.mqttc.loop_forever()
			
		except Exception as e:
			logging.error("The connect error %s,%s"%(e,type(e)))	
		
	
	def send(self,message,channel):
		try:
			(result,mid) = self.mqttc.publish(channel,message,2)
			return result
		except Exception as e:
			logging.error("The send error %s,%s"%(e,type(e)))
		
					


	
