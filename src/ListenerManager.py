from threading import Thread
from ProxyHelper import ProxyHelper
from ConnectionManager import ConnectionManager
from MapEntryListener import MapEntryListener
from EntryEvent import EntryEvent
from ItemEvent import ItemEvent
import socket,time
import threading

class ListenerManager(Thread):
    def __new__(cls):
        if not '__instance' in cls.__dict__:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self):
        Thread.__init__(self)
        self.__connection = ConnectionManager().getConnection()
        self.__listeners = {} #eventTypes
        self.__connection.setTimeout(None)
        self.__proxyHelper = ProxyHelper(self.__connection)
        self.__lock = threading.Lock()
        self.isRunning = False
        
    def run(self):
        while self.isRunning:
            event = self.parseEvent()
            self.notifyListeners(event)
    
    def notifyListeners(self, event):
        if event == None:
            return
        if isinstance(event, EntryEvent):
            if event.eventType == EntryEvent.TYPE_ADDED:
                for listener in self.__listeners[event.listenerType]:
                    listener.entryAdded(event)
            elif event.eventType == EntryEvent.TYPE_REMOVED:
                for listener in self.__listeners[event.listenerType]:
                    listener.entryRemoved(event)
            elif event.eventType == EntryEvent.TYPE_UPDATED:
                for listener in self.__listeners[event.listenerType]:
                    listener.entryUpdated(event)
            elif event.eventType == EntryEvent.TYPE_EVICTED:
                for listener in self.__listeners[event.listenerType]:
                    listener.entryEvicted(event)                                
        elif isinstance(event, ItemEvent):
            if event.eventType == ItemEvent.TYPE_ADDED:
                for listener in self.__listeners[event.listenerType]:
                    listener.itemAdded(event)
            elif event.eventType == ItemEvent.TYPE_REMOVED:
                for listener in self.__listeners[event.listenerType]:
                    listener.itemRemoved(event)
            
    def parseEvent(self):
        try:
            event = None
            value = None
            oldValue = None
            responseLine = self.__connection.readLine()
            if '#' in responseLine:
                count = int (responseLine[responseLine.index('#') + 1:])
                sizeLine = self.__connection.readLine()
                sizes = sizeLine.split()
                if count > 1:
                    key = self.__connection.readObject(int(sizes[0]))
                    value = self.__connection.readObject(int(sizes[1]))
                    if count == 3:
                        oldValue = self.__connection.readObject(int(sizes[1]))
                    self.__connection.readCRLF()
                else :
                    key = self.__connection.readObject(int(sizes[0]))
                    self.__connection.readCRLF()
            responseLine = responseLine.split()
            if responseLine[0] == "EVENT":
                listenerType = responseLine[2]
                if listenerType == MapEntryListener.TYPE_LISTENER or listenerType == "null": # null is for current buggy clientprotocol implementation
                    name = responseLine[3]
                    eventType = responseLine[4]
                    event = EntryEvent(eventType, listenerType, name, key, value, oldValue)
                elif listenerType == "queue":
                    #create ItemEvent
                    raise NotImplementedError
                elif listenerType == "topic":
                    raise NotImplementedError
                else:
                    pass
            return event
        except (socket.error, socket.timeout) as e:
            print "error while reading from socket !!!" , e
            return None
        
    def addListenerOp(self, listener, key, includeValue, name):
        if isinstance(listener, MapEntryListener):
            if key is not None:
                self.__proxyHelper.doOp("MADDLISTENER", 0, 1, key, name, "false" if includeValue == False else "true")
            else:
                self.__proxyHelper.doOp("MADDLISTENER", 0, 0, None, name, "false" if includeValue == False else "true")
        self.registerListener(listener)
        self.isRunning = True
        self.start()

    
    def removeListenerOp(self, listener, key, name):
        if isinstance(listener, MapEntryListener):
            if key is not None:
                self.__proxyHelper.doOp("MREMOVELISTENER", 0, 1, key, name)
            else:
                self.__proxyHelper.doOp("MREMOVELISTENER", 0, 0, None, name)
        self.unregisterListener(listener)
        # do a length check to __listeners and stop the thread if neccessary
    def registerListener(self, listener):
        if self.__listeners.has_key(listener.TYPE_LISTENER):
            if listener not in self.__listeners[listener.TYPE_LISTENER]:
                self.__listeners[listener.TYPE_LISTENER].append(listener) 
        else:
            self.__listeners[listener.TYPE_LISTENER] = [listener]

    def unregisterListener(self, listener):
        if listener in self.__listeners[listener.TYPE_LISTENER]:
            self.__listeners[listener.TYPE_LISTENER].remove(listener)
        