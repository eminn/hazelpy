from TypeSerializer import TypeSerializer
import cPickle as pickle
import time,sys
SERIALIZER_TYPE_OBJECT = 0
SERIALIZER_TYPE_BYTE_ARRAY = 1
SERIALIZER_TYPE_INTEGER = 2
SERIALIZER_TYPE_LONG = 3
SERIALIZER_TYPE_CLASS = 4
SERIALIZER_TYPE_STRING = 5
SERIALIZER_TYPE_DATE = 6
SERIALIZER_TYPE_BIG_INTEGER = 7
SERIALIZER_TYPE_EXTERNALIZABLE = 8
SERIALIZER_TYPE_BOOLEAN = 9
SERIALIZER_PRIORITY_OBJECT = sys.maxint
SERIALIZER_PRIORITY_BYTE_ARRAY = 100
SERIALIZER_PRIORITY_INTEGER = 300
SERIALIZER_PRIORITY_BOOLEAN = 200# changed from 300 because of bool is subclass of int
SERIALIZER_PRIORITY_LONG = 200
SERIALIZER_PRIORITY_CLASS = 500
SERIALIZER_PRIORITY_STRING = 400
SERIALIZER_PRIORITY_DATE = 500
SERIALIZER_PRIORITY_BIG_INTEGER = 600
SERIALIZER_PRIORITY_EXTERNALIZABLE = 50
class DefaultSerializer:
    def __init__(self):
        self.serializers = []
        self.addSerializer(IntegerSerializer())
        self.addSerializer(StringSerializer())
        self.addSerializer(LongSerializer())
        self.addSerializer(BooleanSerializer())
        self.addSerializer(ObjectSerializer())
        self.addSerializer(ByteArraySerializer())
        self.typeSerializer = {}
        self.serializers = sorted(self.serializers)
        for ts in self.serializers:
            self.typeSerializer[ts.getTypeId()] = ts
    def addSerializer(self, serializer):
        self.serializers.append(serializer)
    def write(self, output, obj):
        typeId = -1
        for ts in self.serializers:
            if ts.isSuitable(obj):
                self.typeSerializer[ts.getTypeId()] = ts
                typeId = ts.getTypeId()
                break
        if typeId == -1:
            raise AttributeError("There is no suitable serializer")
        output.writeByte(typeId)
        self.typeSerializer[typeId].write(output, obj)
        
    def read(self, inputStream):
        typeId = inputStream.readByte()
        if typeId == -1:
            raise AttributeError("There is no suitable serializer")
        print typeId
        return self.typeSerializer[typeId].read(inputStream)
class ObjectSerializer(TypeSerializer):
    def priority(self):
        return SERIALIZER_PRIORITY_OBJECT
    def isSuitable(self,obj):
        return isinstance(obj,object)
    def getTypeId(self):
        return SERIALIZER_TYPE_OBJECT
    def read(self,inputStream):
        data = inputStream.readBytes()
        return pickle.loads(data)
    def write(self,output,obj):
        data = bytearray()
        data.extend(pickle.dumps(obj, pickle.HIGHEST_PROTOCOL))
        output.writeBytes(data);
class ByteArraySerializer(TypeSerializer):
    def priority(self):
        return SERIALIZER_PRIORITY_BYTE_ARRAY
    def isSuitable(self,obj):
        return isinstance(obj,bytearray)
    def getTypeId(self):
        return SERIALIZER_TYPE_BYTE_ARRAY
    def read(self,inputStream):
        return inputStream.readBytes()
    def write(self,output,obj):
        output.writeBytes(obj);
class StringSerializer(TypeSerializer):
    def priority(self):
        return SERIALIZER_PRIORITY_STRING
    def isSuitable(self, obj):
        return isinstance(obj, basestring)
    def getTypeId(self):
        return SERIALIZER_TYPE_STRING
    def read(self, inputStream):
        return inputStream.readUTF()
    def write(self, output, obj):
        output.writeUTF(obj)
class IntegerSerializer(TypeSerializer):
    def priority(self):
        return SERIALIZER_PRIORITY_INTEGER
    def isSuitable(self, obj):
        return isinstance(obj, int)
    def getTypeId(self):
        return SERIALIZER_TYPE_INTEGER
    def read(self, inputStream):
        return inputStream.readInt()
    def write(self, output, obj):
        output.writeInt(obj)
class LongSerializer(TypeSerializer):
    def priority(self):
        return SERIALIZER_PRIORITY_LONG
    def isSuitable(self, obj):
        return isinstance(obj, long)
    def getTypeId(self):
        return SERIALIZER_TYPE_LONG
    def read(self, inputStream):
        return inputStream.readLong()
    def write(self, output, obj):
        output.writeLong(obj)
class BooleanSerializer(TypeSerializer):
    def priority(self):
        return SERIALIZER_PRIORITY_BOOLEAN
    def isSuitable(self, obj):
        return isinstance(obj, bool)
    def getTypeId(self):
        return SERIALIZER_TYPE_BOOLEAN
    def read(self, inputStream):
        return inputStream.readBoolean()
    def write(self, output, obj):
        output.writeBoolean(obj)
class DateSerializer(TypeSerializer):
    def priority(self):
        return SERIALIZER_PRIORITY_DATE
    def isSuitable(self, obj):
        return isinstance(obj, time)
    def getTypeId(self):
        return SERIALIZER_TYPE_DATE
    def read(self):
        #return readed integer
        pass
    def write(self, output, obj):
        output.writeLong(long((obj.time() * 1000))) # time in milis
                
        
