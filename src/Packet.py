import bitstring
from struct import pack
class Packet:
    def __init__(self):
        pass
    header = bytearray(b"HZC")
    key = None
    value = None
    name = None
    operation = 59 # map.get
    threadId = -1
    timeout = -1
    ttl = -1
    blockId = -1
    longValue = -1
    version = -1
    callId = 9
    packetVersion = 8
    responseType = 2;
    writerBuffer = bytearray()
    writerHeaderBuffer = bytearray()
    def writeTo(self):
        self.writeHeader()
        self.writerHeaderBuffer.extend(pack("!i",len(self.writerHeaderBuffer)))
        if self.key == None:
            self.writerHeaderBuffer.extend(pack("!i",0)) 
        else:
            pass
            #self.writerBuffer.append(bitstring.BitArray(int=len(str(self.key)), length=32)) # zero 
        if self.value == None:
            self.writerHeaderBuffer.extend(pack("!i",0)) # zero 
        else:
            pass
            #self.writerBuffer.append(bitstring.BitArray(int=len(self.value), length=32)) # zero 
        self.writerHeaderBuffer.extend(pack("!b",self.packetVersion))
        self.writerBuffer.extend(self.writerHeaderBuffer)
        if self.key!=None:
            self.writerBuffer.extend(bytearray(self.key))
        if self.value!=None:
            self.writerBuffer.extend(bytearray(self.value))
    def writeHeader(self):
        self.writerHeaderBuffer.extend(self.header)
        self.writerHeaderBuffer.extend(pack("!h",self.operation))
        self.writerHeaderBuffer.extend(pack("!i",-1)) #blockId
        self.writerHeaderBuffer.extend(pack("!i",-1)) #threadId
        booleans = bitstring.BitArray(8)
        if self.timeout != -1:
            booleans.set(1, 1)
        if self.ttl != -1:
            booleans.set(1, 2)
        #look for long value min ? position 4
        booleans.set(1, 6) # client = true
        booleans.set(1, 7) # lockAddressNull = true
        self.writerHeaderBuffer.extend(booleans)
        if self.timeout != -1:
            self.writerHeaderBuffer.extend(pack("!q",self.timeout))
        if self.ttl != -1:
            self.writerHeaderBuffer.extend(pack("!q",self.ttl))
        if self.longValue != -1:
            self.writerHeaderBuffer.extend(pack("!q",self.longValue))
        self.writerHeaderBuffer.extend(pack("!q",self.callId))
        self.writerHeaderBuffer.extend(pack("!b",self.responseType))
        #name ? 
        self.writerHeaderBuffer.extend(pack("!b",0))
        self.writerHeaderBuffer.extend(pack("!i",-1))#put keyhash
        self.writerHeaderBuffer.extend(pack("!i",-1))#put valuehash
        print self.writerHeaderBuffer
        print len(self.writerHeaderBuffer)
        
    def set(self,name,operation,key,value):
        self.name = name 
        self.operation = operation
        self.key = key
        self.value = value
        

        
