from ProxyHelper import ProxyHelper
from ConnectionManager import ConnectionManager
from MapEntryListener import MapEntryListener
from QueueItemListener import QueueItemListener
from EntryEvent import EntryEvent
from ItemEvent import ItemEvent
import socket
import time
import threading

class ListenerManager(threading.Thread):
    def __new__(cls):
        if not '__instance' in cls.__dict__:
            cls.__instance = object.__new__(cls)
        return cls.__instance 
    
    def __init__(self):
        super(ListenerManager, self).__init__()
        self.__listeners = {} #eventTypes
        self.isRunning = False

    def setProxyHelper(self, proxyHelper):
        self.__proxyHelper = proxyHelper
        self.__proxyHelper.connection.setTimeout(None)

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
            response = self.__proxyHelper.connection.readResponse()
            key = response["binaryData"][0]
            value = response["binaryData"][1]
            if len(response["binaryData"]) == 3:
                oldValue = response["binaryData"][2]
            responseLine = response["commandLine"].split()
            if responseLine[0] == "EVENT":
                listenerType = responseLine[1]
                if listenerType == MapEntryListener.TYPE_LISTENER:
                    name = responseLine[2]
                    eventType = responseLine[3]
                    event = EntryEvent(eventType, listenerType, name, key, value, oldValue)
                elif listenerType == QueueItemListener.TYPE_LISTENER:
                    name = responseLine[2]
                    eventType = responseLine[3]
                    event = ItemEvent(eventType, listenerType, name, value)
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
                self.__proxyHelper.doOp("MADDLISTENER", 1, key, name, "false" if includeValue == False else "true")
            else:
                self.__proxyHelper.doOp("MADDLISTENER", 0, None, name, "false" if includeValue == False else "true")
        elif isinstance(listener, QueueItemListener):
            self.__proxyHelper.doOp("QADDLISTENER", 0, None, name, "false" if includeValue == False else "true")
        self.registerListener(listener)
        print self.__listeners
        self.isRunning = True
        self.start()
    def removeListenerOp(self, listener, key, name):
        print "removeListenerOp"
        if isinstance(listener, MapEntryListener):
            if key is not None:
                self.__proxyHelper.doOp("MREMOVELISTENER", 1, key, name)
            else:
                self.__proxyHelper.doOp("MREMOVELISTENER", 0, None, name)
        self.unregisterListener(listener)
        print self.__listeners
        if len(self.__listeners[listener.TYPE_LISTENER]) < 1:
            print "stopped listenerManager execution"
            self.isRunning = False
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
        