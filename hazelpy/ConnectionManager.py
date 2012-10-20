from Connection import Connection
from random import choice
class ConnectionManager(object):
    __CONNECTION_LIMIT = 2
    __connections = {}
    __count = 0
    def __new__(cls):
        if not '__instance' in cls.__dict__:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def getConnection(self):
        if self.__count < self.__CONNECTION_LIMIT:
            self.__connections[self.__count] = Connection(self.__address,self.__username,self.__password)
            self.__count += 1
            self.__connections[self.__count-1]
            return self.__connections[self.__count-1]
        else:
            return  None
    def setCredentials(self, address,username,password):
        self.__address = address
        self.__username = username
        self.__password = password
    def closeAll(self):
        for key in self.__connections.keys():
            self.__connections[key].close()