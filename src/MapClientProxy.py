from ProxyHelper import ProxyHelper
from ListenerManager import ListenerManager
class MapClientProxy:
    # TODO : extract all data from calling method after making the call.
    # TODO : add noreply option
    def __init__(self , name , connection):
        self.__name = name
        self.__proxyHelper = ProxyHelper(connection)
   
    def addListener(self, listener, key=None, includeValue=False):
        """ If key is provided listener will be notified only for the key,
        otherwise it will notified for all entries in the map 
        If includeValue set to True it will bring  values for the keys with the event"""
        self.__listenerManager = ListenerManager()
        self.__listenerManager.setProxyHelper(self.__proxyHelper)
        listener.listenerManager = self.__listenerManager
        listener.key = key
        listener.name = self.__name
        self.__listenerManager.addListenerOp(listener, key, includeValue, self.__name)
    
    def removeListener(self, listener, key=None):
        self.__listenerManager.removeListenerOp(listener, key, self.__name)   
    
    def put(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        response = self.__proxyHelper.doOp("MPUT", 2, (key, value), self.__name, str(ttl))
        return self.__proxyHelper.readSingleObjectResponse(response)
    
    def putIfAbsent(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        response = self.__proxyHelper.doOp("MPUTIFABSENT", 2, (key, value), self.__name, str(ttl))
        return self.__proxyHelper.readSingleObjectResponse(response)

    def putTransient(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        response = self.__proxyHelper.doOp("MPUTTRANSIENT", 2, (key, value), self.__name, str(ttl))
        return self.__proxyHelper.readSingleObjectResponse(response)
    
    def putAll(self, entries):
        response = self.__proxyHelper.doOp("MPUTALL", 2 * len(entries), entries, self.__name)    
        return self.__proxyHelper.readOKResponse(response)
    
    def putAndUnlock(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        response = self.__proxyHelper.doOp("MPUTANDUNLOCK", 2, (key, value), self.__name)
        return self.__proxyHelper.readOKResponse(response)

    def size(self):
        response = self.__proxyHelper.doOp("MSIZE", 0 , None , self.__name)
        return self.__proxyHelper.readSingleIntResponse(response)
    
    def set(self, key, value, ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        response = self.__proxyHelper.doOp("MSET", 2, (key, value), self.__name, str(ttl))
        return self.__proxyHelper.readOKResponse(response)
    
    def get(self, key):
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MGET", 1, key, self.__name)
        return self.__proxyHelper.readSingleObjectResponse(response)
    
    def getAll(self, keys): 
        for key in keys:
            self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MGETALL", len(keys), keys, self.__name)
        keys = response["binaryData"][::2]
        values = response["binaryData"][1::2]
        result = dict(zip(keys,values))
        return result
    
    def tryLockAndGet(self, key, timeout):
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MTRYLOCKANDGET", 1, key, self.__name, str(timeout))
        return self.__proxyHelper.readSingleObjectResponse(response)

    def tryPut(self, key, value, timeout):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        response = self.__proxyHelper.doOp("MTRYPUT", 2, (key, value), self.__name, str(timeout))
        return self.__proxyHelper.readSingleBoolResponse(response)
   
    def tryLock(self, key, timeout): 
        self.__proxyHelper.check(key)
        response =  self.__proxyHelper.doOp("MTRYLOCK", 1, key, self.__name, str(timeout))
        return self.__proxyHelper.readSingleBoolResponse(response)

    def tryRemove(self, key, timeout):
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MTRYREMOVE", 1, key, self.__name, str(timeout))
        return self.__proxyHelper.readSingleObjectResponse(response)

    def isKeyLocked(self, key): 
        self.__proxyHelper.check(key)
        response =  self.__proxyHelper.doOp("MISKEYLOCKED", 1, key, self.__name)
        return self.__proxyHelper.readSingleBoolResponse(response)

    def lock(self, key):
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MLOCK", 1, key, self.__name)
        return self.__proxyHelper.readSingleBoolResponse(response)

    def unLock(self, key):
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MUNLOCK", 1, key, self.__name)
        return self.__proxyHelper.readOKResponse(response)

    def lockMap(self, timeout):
        response = self.__proxyHelper.doOp("MLOCKMAP", 0, None, self.__name, str(timeout))
        return self.__proxyHelper.readSingleBoolResponse(response)

    def unlockMap(self, timeout):
        return self.__proxyHelper.doOp("MUNLOCKMAP", 0, None, self.__name, str(timeout))
   
    def forceUnlock(self, key): 
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MFORCEUNLOCK", 1, key, self.__name)
        return self.__proxyHelper.readOKResponse(response)   
    
    def containsKey(self, key):  
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MCONTAINSKEY", 1, key, self.__name)
        return self.__proxyHelper.readSingleBoolResponse(response)
   
    def containsValue(self, value):   
        self.__proxyHelper.check(value)
        response =  self.__proxyHelper.doOp("MCONTAINSVALUE", 1, value, self.__name)
        return self.__proxyHelper.readSingleBoolResponse(response)

    def keySet(self):
        response = self.__proxyHelper.doOp("KEYSET", 0, None, "map", self.__name)
        return response["binaryData"]
    
    def remove(self, key):
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MREMOVE", 1, key , self.__name)
        return self.__proxyHelper.readSingleObjectResponse(response)
    
    def removeIfSame(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        response =  self.__proxyHelper.doOp("MREMOVEIFSAME", 2, (key, value), self.__name,)
        return self.__proxyHelper.readSingleBoolResponse(response)
    
    def replaceIfNotNull(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MREPLACEIFNOTNULL", 2, (key, value), self.__name,)
    
    def replaceIfSame(self, key, oldValue, newValue): # ERROR 0 java.lang.String cannot be cast to com.hazelcast.impl.Keys 
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(oldValue)
        self.__proxyHelper.check(newValue)
        return self.__proxyHelper.doOp("MREPLACEIFSAME", 3, (key, oldValue, newValue), self.__name,)
    
    def flush(self):
        response = self.__proxyHelper.doOp("MFLUSH", 0, None, self.__name) 
        return self.__proxyHelper.readOKResponse(response)
    
    def evict(self, key):  
        self.__proxyHelper.check(key)
        response = self.__proxyHelper.doOp("MEVICT", 1, key, self.__name)
        return self.__proxyHelper.readSingleBoolResponse(response)