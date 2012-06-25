from ProxyHelper import ProxyHelper
class MapClientProxy:
    def __init__(self , name , connection):
        self.__name = name
        self.__proxyHelper = ProxyHelper(name, connection)
    def put(self, key, value,ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUT",0,2,(key,value),self.__name,str(ttl))
    def putTransient(self, key, value,ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUTTRANSIENT",0,2,(key,value),self.__name,str(ttl))
    def putAll(self,entries):
        return self.__proxyHelper.doOp("MPUTALL",0,2*len(entries),entries,self.__name)    
    def set(self, key, value,ttl=0):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MSET",0,2,(key,value),self.__name,str(ttl))
    def get(self,key):
        self.__proxyHelper.check(key)
        return self.__proxyHelper.doOp("MGET",0,1,key,self.__name)
    def tryPut(self,key,value,timeout):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MTRYPUT", 0,2, (key,value),self.__name,str(timeout))
