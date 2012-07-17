from ProxyHelper import ProxyHelper
from ListenerManager import ListenerManager
class MapClientProxy:
    FLAG = 0
    def __init__(self , name , connection):
        self.__name = name
        self.__proxyHelper = ProxyHelper(connection)
    def addListener(self, listener, key=None, includeValue=False):
        """ If key is provided listener will be notified only for the key,
        otherwise it will notified for all entries in the map 
        If includeValue set to True it will bring  values for the keys with the event"""
        self.__listenerManager = ListenerManager(self.__proxyHelper)
        listener.listenerManager = self.__listenerManager
        listener.key = key
        listener.name = self.__name
        self.__listenerManager.addListenerOp(listener, key, includeValue, self.__name)
    def removeListener(self, listener, key=None):
        self.__listenerManager.removeListenerOp(listener, key, self.__name)    
    def put(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUT", MapClientProxy.FLAG, 2, (key, value), self.__name, str(ttl))
    def putIfAbsent(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUTIFABSENT", MapClientProxy.FLAG, 2, (key, value), self.__name, str(ttl))
    def putTransient(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUTTRANSIENT", MapClientProxy.FLAG, 2, (key, value), self.__name, str(ttl))
    def putAll(self, entries):
        return self.__proxyHelper.doOp("MPUTALL", MapClientProxy.FLAG, 2 * len(entries), entries, self.__name)    
    def putAndUnlock(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUTANDUNLOCK", MapClientProxy.FLAG, 2, (key, value), self.__name)
    def set(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MSET", MapClientProxy.FLAG, 2, (key, value), self.__name, str(ttl))
    def get(self, key):
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MGET", MapClientProxy.FLAG, 1, key, self.__name)
    def getAll(self, keys): #com.hazelcast.nio.Data cannot be cast to java.lang.Comparable
        for key in keys:
            self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MGETALL", MapClientProxy.FLAG, len(keys), keys, self.__name)
    def tryPut(self, key, value, timeout):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MTRYPUT", MapClientProxy.FLAG, 2, (key, value), self.__name, str(timeout))
    def tryLock(self, key, timeout): # not yet implemented on the server side
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MTRYLOCK", MapClientProxy.FLAG, 1, key, self.__name, str(timeout))
    def isKeyLocked(self, key): # server handler doesn't give reply
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MISKEYLOCKED", MapClientProxy.FLAG, 1, key, self.__name)
    def lock(self, key, timeout):
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MLOCK", MapClientProxy.FLAG, 1, key, self.__name, str(timeout))
    def unLock(self, key):
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MUNLOCK", MapClientProxy.FLAG, 1, key, self.__name)
    def lockMap(self, timeout):
        return self.__proxyHelper.doOp("MLOCKMAP", MapClientProxy.FLAG, 0, None, self.__name, str(timeout))
    def unlockMap(self, timeout):
        return self.__proxyHelper.doOp("MUNLOCKMAP", MapClientProxy.FLAG, 0, None, self.__name, str(timeout))
    def forceUnlock(self, key): 
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MFORCEUNLOCK", MapClientProxy.FLAG, 1, key, self.__name)
    def containsKey(self, key):  
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MCONTAINSKEY", MapClientProxy.FLAG, 1, key, self.__name)
    def containsValue(self, value):   
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MCONTAINSVALUE", MapClientProxy.FLAG, 1, value, self.__name)
    def keySet(self):
        return self.__proxyHelper.doOp("KEYSET", MapClientProxy.FLAG, 0, None, "map", self.__name)
    def remove(self, key):
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MREMOVE", MapClientProxy.FLAG, 1, key , self.__name)
    def removeIfSame(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MREMOVEIFSAME", MapClientProxy.FLAG, 2, (key, value), self.__name,)
    def replaceIfNotNull(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MREPLACEIFNOTNULL", MapClientProxy.FLAG, 2, (key, value), self.__name,)
    def replaceIfSame(self, key, oldValue, newValue): # ERROR 0 java.lang.String cannot be cast to com.hazelcast.impl.Keys 
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(oldValue)
        self.__proxyHelper.check(newValue)
        return self.__proxyHelper.doOp("MREPLACEIFSAME", MapClientProxy.FLAG, 3, (key, oldValue, newValue), self.__name,)
    def flush(self):
        return self.__proxyHelper.doOp("MFLUSH", MapClientProxy.FLAG, 0, None, self.__name)
    def evict(self, key):  
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MEVICT", MapClientProxy.FLAG, 1, key, self.__name)