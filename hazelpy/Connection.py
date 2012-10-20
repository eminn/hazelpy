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
        self.__socket.settimeout(4.0)
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
        command = "AUTH " + username + " " + password + " \r\n"
        self.sendCommand(command)
        response = self.readLine()
        if response == "OK":
            return True
        else:
            return False 
    
    def sendCommand(self, command):
        print command
        self.__socket.sendall(command)
    
    def readLine(self):
        line = []
        while True:
            c = self.__socket.recv(1)
            if c == '\r':
                c2 = self.__socket.recv(1)
                if c2 == '\n':
                    break
            line.append(c)
        return "".join(line)
    
    def readObject(self, size):
        data = bytearray()
        while size > 0:
            chunk = self.__socket.recv(size)
            data.extend(chunk) 
            size -= len(chunk)
        return self.__serializer.toObject(data)
    
    def readCRLF(self):
        while True:
            c = self.__socket.recv(1)
            if c == '\r':
                c2 = self.__socket.recv(1)
                if c2 == '\n':
                    break        
    
    def readResponse(self):
        # todo return only binary array.
        response = {}
        try:
            response["commandLine"] = self.readLine()
            if '#' in response["commandLine"]:
                response["sizeLine"] = self.readLine()
                response["binaryData"] = []
                for size in response["sizeLine"].split():
                    response["binaryData"].append(self.readObject(int(size)))
                self.readCRLF()
            print response
            return response
        except (socket.error, socket.timeout) as e:
            print "error while reading from socket !!!" , e
        return 'NULL'
    
    def setTimeout(self,timeout):
        self.__socket.settimeout(timeout)
    
    def close(self):
        self.__socket.shutdown(socket.SHUT_RDWR)
