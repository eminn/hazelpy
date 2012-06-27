from threading import Thread
from ProxyHelper import ProxyHelper
from ConnectionManager import ConnectionManager
from MapEntryListener import MapEntryListener
import socket
class ListenerManager(Thread):
    def __new__(cls):
        if not '__instance' in cls.__dict__:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self):
        Thread.__init__(self)
        self.__connection = ConnectionManager().getConnection()
        self.__listeners = []
        self.__connection.setTimeout(None)
        self.__proxyHelper = ProxyHelper(self.__connection)
        
    def run(self):
        while True:
            self.parseEvent()
            #notifyListeners()
            
    def parseEvent(self):
        try:
            responseLine = self.__connection._readLine()
            print responseLine.split()
            if '#' in responseLine:
                count = int (responseLine[responseLine.index('#') + 1:len(responseLine)])
                sizeLine = self.__connection._readLine()
                sizes = sizeLine.split()

            print responseLine
        except (socket.error, socket.timeout) as e:
            print "error while reading from socket !!!" , e
        
    def addListenerOp(self, listener, key, includeValue, name):
        if isinstance(listener, MapEntryListener):
            if key is not None:
                self.__proxyHelper.doOp("MADDLISTENER", 0, 1, key, name, "false" if includeValue == False else "true")
            else:
                self.__proxyHelper.doOp("MADDLISTENER", 0, 0, None, name, "false" if includeValue == False else "true")
    def registerListener(self, listener):
        if listener not in self.__listeners:
            self.__listeners.append(listener)
        #    self.__proxyHelper.doOp(command, flag, argsCount, binary)
        print listener
        pass
    def removeListener(self, listener):
        if listener in self.__listeners:
            self.__listeners.remove(listener)
    
