from AbstractSerializer import AbstractSerializer
from DataSerializer import DataSerializer
from DefaultSerializer import DefaultSerializer
import types

class ProxyHelper:
    def __init__(self, connection):
        self.connection = connection
        self.__newline = '\r\n'
        self.__serializer = AbstractSerializer(DataSerializer(), DefaultSerializer())
    def check(self, obj):
        if obj == None:
            raise ValueError("Object cannot be null")
    def doOp(self, command, argsCount=0, binary=None, *c_args):
        count = "" if argsCount == 0 else ' #' + str(argsCount)
        command_str = command  + ' ' + ' '.join(c_args) + count + self.__newline
       # command_str = []
       # command_str.append(command)
       # command_str.append(" ")
       # command_str.append(" ".join(c_args))
       # command_str.append(count)
       # command_str.append(self.__newline)
        if argsCount != 0 and binary != None:
            size = []
            data = bytearray()
            if isinstance(binary, (types.ListType, types.TupleType)):
                for item in binary:
                    byte = self.__serializer.toByte(item)
                    size.append(str(len(byte)))
                    size.append(" ") 
                    data.extend(byte)
            elif isinstance(binary, types.DictionaryType):
                for key in binary.keys():
                    value = list(self.__serializer.toByte(binary[key]))
                    key = list(self.__serializer.toByte(key))
                    size.append(str(len(key)) )
                    size.append(" ")
                    size.append(str(len(value)))
                    size.append(" ")
                    data.extend(key)
                    data.extend(value)
            else:
                byte = self.__serializer.toByte(binary)
                size.append(str(len(byte)))
                size.append(" ")
                data.extend(byte)
            size.pop()
           # command_str.append("".join(size))
           # command_str.append(self.__newline)
           # command_str.append(str(data))
           # command_str.append(self.__newline)
            command_str += "".join(size) + self.__newline
            command_str += data + self.__newline
       # return self.connection.sendCommand("".join(command_str))
        self.connection.sendCommand(command_str)
        # TODO : add noreply option
        # if noreply == True:
        #     return
        # else:
        #     return  self.connection.readResponse()
        return  self.connection.readResponse()

    def readSingleObjectResponse(self, response):
        if "sizeLine" in response:
            obj = response["binaryData"][0]
            return obj
        else:
            return self.readOKResponse(response)          
    def readSingleIntResponse(self, response):
        commandLine = response["commandLine"].split()
        return int(commandLine[1])
    def readSingleBoolResponse(self, response):
        commandLine = response["commandLine"].split()
        if commandLine[1] == "true":
            return True
        elif commandLine[1] == "false":
            return False
        else:
            return None
    def readOKResponse(self, response):
        if response["commandLine"] == "OK \r\n" or response["commandLine"] == "OK":
            return True
        else:
            return False
