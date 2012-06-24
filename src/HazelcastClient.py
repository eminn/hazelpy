from Connection import Connection
from MapClientProxy import MapClientProxy
class HazelcastClient:
	def __init__(self,host='localhost',port=5701,username='dev',password='dev-pass'):
		self.__connection = Connection(host, port)
		self.authenticate(username, password)

	
	def getMap(self,name):
		return MapClientProxy(name,self.__connection)
	def authenticate(self,username,password):
		command = "AUTH " + "0 " + username + " " + password + " \r\n"
		self.__connection.send_command(command)