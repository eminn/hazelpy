from TypeSerializer import TypeSerializer
from DataSerializable import DataSerializable
SERIALIZER_TYPE_DATA = 0
class DataSerializer(TypeSerializer):
    def priority(self):
        return 0
    def isSuitable(self,object):
        return isinstance(object,DataSerializable)
    def getTypeId(self):
        return SERIALIZER_TYPE_DATA
    def read(self,input):
        raise NotImplementedError
    def toClassName(self,object):
        return object.__class__.__name__
    def write(self,output,object):
        output.writeUTF(self.toClassName(object))
        object.writeData(output)