from ConnectionManager import ConnectionManager
from MapClientProxy import MapClientProxy
from QueueClientProxy import QueueClientProxy
from GeneralClientProxy import GeneralClientProxy
class HazelcastClient:
	def __init__(self,host='localhost',port=5701,username='dev',password='dev-pass'):
		self.__connectionManager = ConnectionManager()
		self.__connectionManager.setCredentials( (host, port) , username, password)
		self.__connection = self.__connectionManager.getConnection()
		self.__connection.connect()
		self.__generalClientProxy = GeneralClientProxy(self.__connection)
		
	
	def close(self):
		self.__connectionManager.closeAll()
	
	def instances(self):
		return self.__generalClientProxy.instances()
	
	def members(self):
		return self.__generalClientProxy.members()
	
	def ping(self):
		return self.__generalClientProxy.ping()
	
	def destroy(self, type, name):
		return self.__generalClientProxy.destroy(type,name)
	
	def getMap(self,name):
		return MapClientProxy(name,self.__connection)
	
	def getQueue(self,name):
		return QueueClientProxy(name,self.__connection)
	
	def clusterTime(self):
		return self.__generalClientProxy.clusterTime()
	
	def partitions(self,key=None):
		return self.__generalClientProxy.partitions(key)