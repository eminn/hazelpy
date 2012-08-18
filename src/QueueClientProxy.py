from ProxyHelper import ProxyHelper
from ListenerManager import ListenerManager
class QueueClientProxy:
    def __init__(self , name , connection):
        self.__name = name
        self.__proxyHelper = ProxyHelper(connection)
    def addListener(self, listener, includeValue=True):
        self.__listenerManager = ListenerManager(self.__proxyHelper)
        listener.listenerManager = self.__listenerManager
        listener.name = self.__name
        self.__listenerManager.addListenerOp(listener, None, includeValue, self.__name)
    def offer(self, element, timeout=0):
        self.__proxyHelper.check(element)
        return self.__proxyHelper.doOp("QOFFER", 1, element, self.__name, str(timeout))
    def put(self, element):
        return self.__proxyHelper.doOp("QPUT", 0, None, self.__name)
    def poll(self, timeout=0):
        return self.__proxyHelper.doOp("QPOLL", 0, None, self.__name, str(timeout))
    def take(self, timeout=0):
        return self.__proxyHelper.doOp("QTAKE", 0, None, self.__name)
    def size(self):
        return self.__proxyHelper.doOp("QSIZE", 0, None, self.__name)
    def peek(self):
        return self.__proxyHelper.doOp("QPEEK", 0, None, self.__name)
    def remove(self, element):
        self.__proxyHelper.check(element)
        return self.__proxyHelper.doOp("QREMOVE", 1, element, self.__name)
    def remainingCapacity(self):
        return self.__proxyHelper.doOp("QREMCAPACITY", 0, None, self.__name)
    def entries(self):
        return self.__proxyHelper.doOp("QENTRIES", 0, None, self.__name)
