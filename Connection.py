import socket
from DefaultSerializer import DefaultSerializer
from AbstractSerializer import AbstractSerializer
from DataSerializer import DataSerializer

class Connection:
    buffersize = 16 << 10
    newline = '\r\n'
    protocol = 'P01' + newline
    serializer = AbstractSerializer(DataSerializer(), DefaultSerializer())
    def __init__(self, host, port):
        self.__address = (host, port)
        self.__socket = socket.socket()
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.__socket.settimeout(3.0)
        try:
            self.__socket.connect(self.__address)
            self.__socket.sendall(self.protocol)
        except socket.error:
            print 'Socket connect failed!'
            self.__socket.close()

    def send_command(self, command):
        self.__socket.sendall(command)
        print command
        self.read_response()
        pass

    def pack_command(self, command, flag=0, argsCount=0, binary=None, *c_args):
        command_str = command + ' ' + str(flag) + ' ' + ' '.join(c_args) + ' #' + str(argsCount) + self.newline
        if argsCount != 0 and binary != None:
            size = ""
            data = bytearray()
            for item in binary:
                bytes = self.serializer.toByte(item)
                size += str(len(bytes)) + " " 
                data.extend(bytes)
                print list(data)
            command_str += size + self.newline
            command_str += data
            
            print "pack binary data"
        self.send_command(command_str)

        
    def read_response(self):
        try:
            buffer = self.__socket.recv(4096)
            print buffer
        except socket.error, socket.timeout:
                print "error while reading from socket !!!"
        pass


    def __str__(self):
        return "Connection -> [" + str(self.__address) + "]"

    def close(self):
        self.__socket.close()
