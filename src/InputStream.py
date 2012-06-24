from struct import unpack
class InputStream:
    FORMAT_STRING_BOOLEAN = "!?" # bool
    FORMAT_STRING_BYTE = "!b" # 1-byte
    FORMAT_STRING_SHORT = "!h" # 2-byte
    FORMAT_STRING_INTEGER = "!i" # 4-byte
    FORMAT_STRING_LONG = "!q" # 8-byte
    def __init__(self):
        self.buf = bytearray()
    def setData(self,ba):
        self.buf.extend(ba)
    def flush(self):
        del self.buf[:]
    def readBoolean(self):
        print unpack(self.FORMAT_STRING_BOOLEAN , self.buf)
    def readInt(self):
        try:
            integer = unpack(self.FORMAT_STRING_INTEGER , str(self.buf[:4]))
            self.buf = self.buf[4:]
            return int(integer[0])
        except Exception as e:
            print e
    def readByte(self):
        byte = unpack(self.FORMAT_STRING_BYTE, str(self.buf[:1]))
        self.buf = self.buf[1:]
        return byte[0]