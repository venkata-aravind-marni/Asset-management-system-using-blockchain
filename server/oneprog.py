import ast
import paho.mqtt.client as mqtt
import logging
import ConfigParser
# import Savoir
import simplejson as json
import logging


LOG_FILENAME = 'LogFiles/oneProg.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format='%(asctime)s, %(levelname)s, %(message)s', datefmt='%Y-%m-%d %H:%M:%S')




class Multichainpython:

	def __init__(self,rpcuser,rpcpasswd,rpchost,rpcport,chainname):
		self.rpcuser = rpcuser
		self.rpcpasswd = rpcpasswd
		self.rpchost = rpchost
		self.rpcport = rpcport
		self.chainname = chainname

	def multichainConnect(self):
		try:
			# The api connection 
			self.api = Savoir.Savoir(self.rpcuser, self.rpcpasswd, self.rpchost, self.rpcport, self.chainname)
			return self.api
		except Exception as e:
			logging.error("The multichainConnect error %s,%s"%(e,type(e)))
			return False
	def gettotalbalances(self):
		try:
		    totalbalances = self.api.gettotalbalances()
		    return totalbalances
		except Exception as e:
		    print e
		    return False
	def getburnaddress(self):
		try:
			burnaddress = self.api.getinfo()["burnaddress"]
			return burnaddress
		except Exception as e:
			print e
			return False	    
	def accountAddress(self):
		try:
			accountaddress = self.api.getaddressesbyaccount("")[0]
			return accountaddress
		except Exception as e:
			logging.error("The accountAddress error %s,%s"%(e,type(e)))
			return False
	def issueAsset(self,assetaddress,assetdetails,assetquantity,assetunit,assetnativeamount,assetcustomfield):
		try:
			issueasset = self.api.issue(assetaddress,assetdetails,assetquantity,assetunit,assetnativeamount,assetcustomfield)
			return issueasset
		except Exception as e:
			logging.error("The issueAsset error %s,%s"%(e,type(e)))	
			return False
	def issueMoreAsset(self,assetaddress,assetname,assetcustomfield):
		try:
			issueassetmore = self.api.issuemore(assetaddress,assetname,0,0,assetcustomfield)
			return issueassetmore
		except Exception as e:
			logging.error("The issueMoreAsset error %s,%s"%(e,type(e)))		
			return False

	def sendAsset(self,assetaddress,assetname,assetquantity):
		try:
			sendasset = self.api.sendassettoaddress(assetaddress,assetname,assetquantity)
			return sendasset
		except Exception as e:
			logging.error("The sendAsset error %s,%s"%(e,type(e)))			
			return False
	def preparelockunspentexchange(self,asset):
		try:
			preparelock = self.api.preparelockunspent(asset)
			return preparelock
		except Exception as e:
			logging.error("The preparelockunspentexchange error is %s,%s"%(e,type(e)))		
			return false
	def createrawExchange(self,txid,vout,asset):
		try:
			createexchange = self.api.createrawexchange(txid,vout,asset)
			return createexchange
		except Exception as e:
			logging.error("The createrawExchange error is %s,%s"%(e,type(e)))		
			return False

	def decoderawExchange(self,createex_hexBlob):
		try:
			decodeexchange = self.api.decoderawexchange(createex_hexBlob)
			return decodeexchange
		except Exception as e:
			logging.error("The decoderawExchange error %s,%s"%(e,type(e)))		
			return False

			
	def appendrawExchange(self,createex_hexBlob,txid,vout,asset):
		try:
			appendexchange = self.api.appendrawexchange(createex_hexBlob,txid,vout,asset)
			return appendexchange
		except Exception as e:
			logging.error("The appendrawExchange error %s,%s"%(e,type(e)))
			return False
	def sendrawTransaction(self,appex_hexBlob):
		try:
			sendexchange = self.api.sendrawtransaction(appex_hexBlob)
			return sendexchange
		except Exception as e:
			logging.error("The sendrawTransaction error %s,%s"%(e,type(e)))		
			return False
	
	# - ------- - - - - - -- Following functions are for querying the asset ---- - - - - 
	
	def subscribeToasset(self,assetname):
		try:
			subscrbtoasst = self.api.subscribe(assetname)
			return subscrbtoasst
		except Exception as e:
			logging.error("The subscribeToasset error %s,%s"%(e,type(e)))
			return False	
	def queryAssetTransactions(self,assetname):
		try:
			queryassttrans = self.api.listassettransactions(assetname)
			return queryassttrans 
		except Exception as e:
			logging.error("The queryAssetTransactions error %s,%s"%(e,type(e)))		 
			return False
	
	def queryassetsdetails(self,assetname):
		try:
			assetdetails = self.api.listassets(assetname,True) # Here True is for fetching full details its called verbose
			return assetdetails
		except Exception as e:
			logging.error("The queryassetdetails error %s,%s"%(e,type(e)))		


class MQtt:
	def __init__(self,host,port,subTopic,timealive=60):
		self.host = host
		self.port = port
		self.timealive = timealive
		self.payload = None
		self.subTopic = subTopic
		self.pubTopic = "equipchain-server-sender"

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
		    if (self.payload["type"] == "REQ"):
/
		    	if (self.payload["op"] == "LOGIN"):
		    		username = self.payload["details"]["username"]
		    		password = self.payload["details"]["password"]

		    		if (username == UserData["username"] and password == UserData["password"]):
		    			message = {"sender":"SERVER","type":"RESP","op":"LOGIN","details":{"returnVal":0}}
		    		else:
		    			message = {"sender":"SERVER","type":"RESP","op":"LOGIN","details":{"returnVal":1}}
		    	print message		
		    	self.send(json.dumps(message))	


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
		
	
	def send(self,message):
		try:
			(result,mid) = self.mqttc.publish(self.pubTopic,message,2)
			return result
		except Exception as e:
			logging.error("The send error %s,%s"%(e,type(e)))
		


if __name__ == '__main__':
	
	UserData = {"username":"pramod","password":"1234"}


	filename = "config.ini"
	cf = ConfigParser.ConfigParser()
	cf.read(filename)



	# MQTT DETIALS
	host = cf.get("Mqtt","host")
	port = cf.get("Mqtt","port")
	subTopic = cf.get("Mqtt","subTopic")

	mq = MQtt(host,port,subTopic)			
	mq.connect()
			


