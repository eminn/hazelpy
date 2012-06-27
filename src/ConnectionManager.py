from Connection import Connection
from random import choice
class ConnectionManager(object):
    __CONNECTION_LIMIT = 5
    __connections = {}
    def __new__(cls):
        if not '__instance' in cls.__dict__:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def createConnections(self,(host,port),username,password):
        if len(self.__connections) > 4:
            return
        for x in range(0,self.__CONNECTION_LIMIT):
            self.__connections[x] = Connection(x,(host,port),username,password)
    def getConnection(self):
        if len(self.__connections) > 0:
            # popitem
            return self.__connections.pop(choice(self.__connections.keys()))
        else:
            return None

    def putBack(self,connection):
        if len(self.__connections) < 5:
            connection.close()
            self.__connections[connection.id] = connection
    def closeAll(self):
        for key in self.__connections.keys():
            self.__connections[key].close()