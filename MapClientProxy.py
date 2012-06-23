from ProxyHelper import ProxyHelper
class MapClientProxy:
    def __init__(self , name , connection):
        self.__name = name
        self.__proxyHelper = ProxyHelper(name, connection)
    def put(self, key, value):
        self.__proxyHelper.check(key)
        self.__proxyHelper.check(value)
        return self.__proxyHelper.doOp("MPUT",self.__name,key,value)

      
    pass
