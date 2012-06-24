from DefaultSerializer import DefaultSerializer
from AbstractSerializer import AbstractSerializer
from DataSerializer import DataSerializer
import collections

class ProxyHelper:
    def __init__(self, name, connection):
        self.__name = name
        self.__connection = connection
        self.__newline = '\r\n'
        self.__serializer = AbstractSerializer(DataSerializer(), DefaultSerializer())

    def check(self, obj):
        if obj == None:
            print "object cannot be null" 
        
    def doOp(self, command, flag=0, argsCount=0, binary=None, *c_args):
        command_str = command + ' ' + str(flag) + ' ' + ' '.join(c_args) + ' #' + str(argsCount) + self.__newline
        if argsCount != 0 and binary != None:
            size = ""
            data = bytearray()
            if isinstance(binary,collections.Iterable):
                for item in binary:
                    byte = self.__serializer.toByte(item)
                    size +=str(len(byte)) + " " 
                    data.extend(byte)
                    print list(data)
            else:
                byte = self.__serializer.toByte(binary)
                size += str(len(byte)) + " "
                data.extend(byte)
                print list(data)
            command_str += size + self.__newline
            command_str += data
        print command_str
        return self.__connection.send_command(command_str)

