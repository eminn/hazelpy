class ProxyHelper:
    def __init__(self, name, connection):
        self.__name = name
        self.__connection = connection
        pass

    def check(self, object):
        if object == None:
            print "object cannot be null" 
            
    def doOp(self,command,name,key,value):
        self.__connection.pack_command(command,0,2,(key,value),name,"0")
        pass
        