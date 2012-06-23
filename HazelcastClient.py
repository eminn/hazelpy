from Connection import Connection
from MapClientProxy import MapClientProxy
class HazelcastClient:
	def __init__(self,host='localhost',port=5701,username='dev',password='dev-pass'):
		self.__connection = Connection(host, port)
		self.authenticate(username, password)

	
	def getMap(self,name):
		return MapClientProxy(name,self.__connection)
	def authenticate(self,username,password):
		self.__connection.pack_command("AUTH",1,0,None,username,password)