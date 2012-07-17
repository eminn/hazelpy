import socket
from DefaultSerializer import DefaultSerializer
from AbstractSerializer import AbstractSerializer
from DataSerializer import DataSerializer
class Connection:
    protocol = 'P01 \r\n'
    def __init__(self,(host, port), username, password):
        self.address = (host, port)
        self.__username = username 
        self.__password = password
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.__socket.settimeout(10.0)
        self.__serializer = AbstractSerializer(DataSerializer(), DefaultSerializer())
    def connect(self):
        try:
            self.__socket.connect(self.address)
            self.__socket.sendall(self.protocol)
            self.authenticate(self.__username, self.__password)
        except socket.error:
            print 'Socket connect failed!'
            self.__socket.close()
    
    def authenticate(self, username, password):
        command = "AUTH " + "0 " + username + " " + password + " \r\n"
        self.sendCommand(command)
    def sendCommand(self, command):
        self.__socket.sendall(command)
        return self.readResponse()
 
    def readLine(self):
        line = ""
        while True:
            c = self.__socket.recv(1)
            if c == '\r':
                c2 = self.__socket.recv(1)
                if c2 == '\n':
                    break
            line += c
        return line
    def readObject(self, size):
        data = ""
        while len (data) < size:
            data += self.__socket.recv(size - len(data))
        return self.__serializer.toObject(data)
    def readCRLF(self):
        while True:
            c = self.__socket.recv(1)
            if c == '\r':
                c2 = self.__socket.recv(1)
                if c2 == '\n':
                    break        
    def readResponse(self):
        try:
            responseLine = self.readLine()
            if '#' in responseLine:
                count = int (responseLine[responseLine.index('#') + 1:])
                sizeLine = self.readLine()
                sizes = sizeLine.split()
                objects = []
                if count > 1: # test other for this old : lines>1
                    for size in sizes:
                        objects.append(self.readObject(int(size)))
                    self.readCRLF()
                    return objects
                else :
                    obj = self.readObject(int(sizes[0]))
                    self.readCRLF()
                    return obj
            else:
                if responseLine == 'OK 0':
                    return True
                elif len(responseLine.split()) > 2:
                    if responseLine.split()[2] == "true":
                        return True
                    elif responseLine.split()[2] == "false" or responseLine.split()[2] == "unknown_command": 
                        return False 
                    elif responseLine.split()[1] == "ERROR":
                        return False
                    else:
                        #print responseLine
                        return int(responseLine.split()[2])
                else:
                    return responseLine
        except (socket.error, socket.timeout) as e:
            print "error while reading from socket !!!" , e

    def setTimeout(self,timeout):
        self.__socket.settimeout(timeout)
    def close(self):
        self.__socket.shutdown(socket.SHUT_RDWR)
