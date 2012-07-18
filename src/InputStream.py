from struct import unpack
class InputStream:
    FORMAT_STRING_BOOLEAN = "!?" # bool
    FORMAT_STRING_BYTE = "!b" # 1-byte
    FORMAT_STRING_SHORT = "!h" # 2-byte
    FORMAT_STRING_INTEGER = "!i" # 4-byte
    FORMAT_STRING_LONG = "!q" # 8-byte
    def __init__(self):
        self.__buf = bytearray()
    def setData(self,ba):
        self.__buf.extend(ba)
    def flush(self):
        del self.__buf[:]
    def readBoolean(self):
        boolean = unpack(self.FORMAT_STRING_BOOLEAN , str(self.__buf[:1]))
        del self.__buf[:1]
        return boolean[0] 
    def readByte(self):
        byte = unpack(self.FORMAT_STRING_BYTE, str(self.__buf[:1]))
        del self.__buf[:1]
        return byte[0]
    def readShort(self):
        short = unpack(self.FORMAT_STRING_SHORT , str(self.__buf[:2]))
        del self.__buf[:2]
        return short[0]
    def readInt(self):
        try:
            integer = unpack(self.FORMAT_STRING_INTEGER , str(self.__buf[:4]))
            del self.__buf[:4]
            return int(integer[0])
        except Exception as e:
            print e
    def readBytes(self):
        size = self.readInt()
        data = []
        while size > 0 :
            data.append(self.readByte())
            size -= 1
        return "".join(data)
    def readLong(self):
        longint = unpack(self.FORMAT_STRING_LONG, str(self.__buf[:8]))
        del self.__buf[:8]
        return longint[0]
    def readUTF(self):
        isNull = self.readBoolean()
        if isNull : return None
        length = self.readInt()
        utflen = self.readShort()
        utfstr = (self.__buf[:utflen]).decode('utf-8')
        return str(utfstr)