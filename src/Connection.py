import socket
from DefaultSerializer import DefaultSerializer
from AbstractSerializer import AbstractSerializer
from DataSerializer import DataSerializer
class Connection:
    protocol = 'P01 \r\n'
    def __init__(self, host, port):
        self.__address = (host, port)
        self.__socket = socket.socket()
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.__socket.settimeout(3.0)
        self.__serializer = AbstractSerializer(DataSerializer(), DefaultSerializer())
        try:
            self.__socket.connect(self.__address)
            self.__socket.sendall(self.protocol)
        except socket.error:
            print 'Socket connect failed!'
            self.__socket.close()

    def send_command(self, command):
        self.__socket.sendall(command)
        return self.read_response()

    def __readLine(self):
        line = ""
        while True:
            c = self.__socket.recv(1)
            if c == '\r':
                c2 = self.__socket.recv(1)
                if c2 == '\n':
                    break
            line += c
        return line
    def __readObject(self,size):
        data = ""
        while len (data) < size:
            data += self.__socket.recv(size- len(data))
        return self.__serializer.toObject(data)

    def read_response(self):
        try:
            responseLine = self.__readLine()
            print responseLine
            if '#' in responseLine:
                lines = int (responseLine[responseLine.index('#')+1])
                sizeLine = self.__readLine()
                sizes = sizeLine.split()
                objects = []
                if lines > 1:
                    for size in sizes:
                        objects.append(self.__readObject(int(size)))
                    return objects
                else :
                    return self.__readObject(int(sizes[0]))
            else:
                if responseLine == 'OK 0':
                    return True
                elif len(responseLine.split()) > 2:
                    if responseLine.split()[2] == "true":
                        return True
                    elif responseLine.split()[2] == "false":
                        return False 
                    elif responseLine.split()[1] == "ERROR":
                        return False
                    else:
                        return False
                else:
                    return responseLine
        except (socket.error, socket.timeout) as e:
            print "error while reading from socket !!!" , e

    def __str__(self):
        return "Connection -> [" + str(self.__address) + "]"

    def close(self):
        self.__socket.close()
