import socket
from DefaultSerializer import DefaultSerializer
from AbstractSerializer import AbstractSerializer
from DataSerializer import DataSerializer
class Connection:
    buffersize = 16 << 10
    protocol = 'P01 \r\n'
    def __init__(self, host, port):
        self.__address = (host, port)
        self.__socket = socket.socket()
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.__socket.settimeout(100.0)
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

        
    def read_response(self):
        try:
            buff = self.__socket.recv(4096)
            if "\r\n" not in buff:
                return None
            else:
                response = [x for x in buff.rsplit("\r\n") if x]
                if len(response) > 1:
                    size = int(response[1])
                    data = response[2]
                    while len (data) < size:
                        data += self.__socket.recv(size- len(data))
                    return self.__serializer.toObject(data)
                else:
                    if response[0] == 'OK 0':
                        return True
                    elif len(response[0].split()) > 2:
                        if response[0].split()[2] == "true":
                            return True
                        else:
                            return False
                    else:
                        return response[0]
            # response = filter(None,buff.rsplit("\r\n"))
        except (socket.error, socket.timeout) as e:
            print "error while reading from socket !!!" , e


    def __str__(self):
        return "Connection -> [" + str(self.__address) + "]"

    def close(self):
        self.__socket.close()
