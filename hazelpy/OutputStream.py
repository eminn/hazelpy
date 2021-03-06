from struct import pack
class OutputStream:
	FORMAT_STRING_BOOLEAN = "!?" # bool
	FORMAT_STRING_BYTE = "!b" # 1-byte
	FORMAT_STRING_SHORT = "!h" # 2-byte
	FORMAT_STRING_INTEGER = "!i" # 4-byte
	FORMAT_STRING_LONG = "!q" # 8-byte
	def __init__(self):
		self.buf = bytearray()
	def flush(self):
		del self.buf[:]
	def writeUTF(self, value):
		isnull = False
		if len(value) == 0:
			isnull = True
		self.writeBoolean(isnull)
		if isnull:
			return
		byte = unicode (value,"utf-8")
		byte = byte.encode("utf-8")
		self.writeInt(len(byte))
		self.writeShort(len(byte))
		self.buf.extend(byte)
	def writeBoolean(self, value):
		self.buf.extend(pack(self.FORMAT_STRING_BOOLEAN,value))
	def writeLong(self,value):
		self.buf.extend(pack(self.FORMAT_STRING_LONG,value))
	def writeInt(self, value):
		self.buf.extend(pack(self.FORMAT_STRING_INTEGER,value))
	def writeShort(self,value):
		self.buf.extend(pack(self.FORMAT_STRING_SHORT,value))
	def writeByte(self,value):
		self.buf.extend(pack(self.FORMAT_STRING_BYTE,value))
	def writeBytes(self,value):
		self.writeInt(len(value))
		for byte in value:
			self.writeByte(byte)