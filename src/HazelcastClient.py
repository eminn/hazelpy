from ConnectionManager import ConnectionManager
from MapClientProxy import MapClientProxy
class HazelcastClient:
	def __init__(self,host='localhost',port=5701,username='dev',password='dev-pass'):
		self.__connectionManager = ConnectionManager()
		self.__connectionManager.createConnections((host, port), username, password)
		self.__connection = self.__connectionManager.getConnection()
	def close(self):
		self.__connectionManager.putBack(self.__connection)
	def getMap(self,name):
		return MapClientProxy(name,self.__connection)
