from TypeSerializer import TypeSerializer
from DataSerializable import DataSerializable
SERIALIZER_TYPE_DATA = 0
class DataSerializer(TypeSerializer):
    def priority(self):
        return 0
    def isSuitable(self,obj):
        return isinstance(obj,DataSerializable)
    def getTypeId(self):
        return SERIALIZER_TYPE_DATA
    def read(self,inputStream):
        raise NotImplementedError
    def toClassName(self,obj):
        return obj.__class__.__name__
    def write(self,output,obj):
        output.writeUTF(self.toClassName(obj))
        obj.writeData(output)