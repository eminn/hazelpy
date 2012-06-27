from ProxyHelper import ProxyHelper
from ListenerManager import ListenerManager
class MapClientProxy:
    def __init__(self , name , connection):
        self.__name = name
        self.__proxyHelper = ProxyHelper(connection)
    def addListener(self,listener,key=None,includeValue=False):
        """ If key is provided listener will be notified only for the key,
        otherwise it will notified for all entries in the map 
        If includeValue set to True it will bring  values of the keys with every event"""
        self.__listenerManager = ListenerManager()
        self.__listenerManager.addListenerOp(listener,key,includeValue,self.__name)
        self.__listenerManager.registerListener(listener)
        self.__listenerManager.start()
    
    def put(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUT", 0, 2, (key, value), self.__name, str(ttl))
    def putIfAbsent(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUTIFABSENT", 0, 2, (key, value), self.__name, str(ttl))
    def putTransient(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUTTRANSIENT", 0, 2, (key, value), self.__name, str(ttl))
    def putAll(self, entries):
        return self.__proxyHelper.doOp("MPUTALL", 0, 2 * len(entries), entries, self.__name)    
    def putAndUnlock(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUTANDUNLOCK", 0, 2, (key, value), self.__name)
    def set(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MSET", 0, 2, (key, value), self.__name, str(ttl))
    def get(self, key):
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MGET", 0, 1, key, self.__name)
    def getAll(self, keys): #com.hazelcast.nio.Data cannot be cast to java.lang.Comparable
        for key in keys:
            self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MGETALL", 0, len(keys), keys, self.__name)
    def tryPut(self, key, value, timeout):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MTRYPUT", 0, 2, (key, value), self.__name, str(timeout))
    def tryLock(self, key, timeout): # not yet implemented on the server side
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MTRYLOCK", 0, 1, key, self.__name, str(timeout))
    def isKeyLocked(self, key): # server handler doesn't give reply
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MISKEYLOCKED", 0, 1, key, self.__name)
    def lock(self, key, timeout):
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MLOCK", 0, 1, key, self.__name, str(timeout))
    def unLock(self, key):
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MUNLOCK", 0, 1, key, self.__name)

    def lockMap(self, timeout):
        return self.__proxyHelper.doOp("MLOCKMAP", 0, 0, None, self.__name, str(timeout))
    def unlockMap(self, timeout):
        return self.__proxyHelper.doOp("MUNLOCKMAP", 0, 0, None, self.__name, str(timeout))
    def forceUnlock(self, key): 
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MFORCEUNLOCK", 0, 1, key, self.__name)
    def containsKey(self, key):  
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MCONTAINSKEY", 0, 1, key, self.__name, "map")
    def containsValue(self, value):   
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MCONTAINSVALUE", 0, 1, value, self.__name, "map")
    def keySet(self):
        return self.__proxyHelper.doOp("KEYSET", 0, 0, None, "map", self.__name)
    def removeIfSame(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MREMOVEIFSAME", 0, 2, (key, value), self.__name,)
    def replaceIfNotNull(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MREPLACEIFNOTNULL", 0, 2, (key, value), self.__name,)
    def replaceIfSame(self, key, oldValue, newValue): # ERROR 0 java.lang.String cannot be cast to com.hazelcast.impl.Keys 
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(oldValue)
        self.__proxyHelper.check(newValue)
        return self.__proxyHelper.doOp("MREPLACEIFSAME", 0, 3, (key, oldValue, newValue), self.__name,)
    def flush(self):
        return self.__proxyHelper.doOp("MFLUSH", 0, 0, None, self.__name)
    def evict(self, key):  
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MEVICT", 0, 1, key, self.__name)
