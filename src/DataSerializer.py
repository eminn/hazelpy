from TypeSerializer import TypeSerializer
from DataSerializable import DataSerializable
SERIALIZER_TYPE_DATA = 0
class DataSerializer(TypeSerializer):
    nameCache = {}
    def priority(self):
        return 0
    def isSuitable(self,obj):
        return isinstance(obj,DataSerializable)
    def getTypeId(self):
        return SERIALIZER_TYPE_DATA
    def read(self,inputStream):
        className = inputStream.readUTF()
        print "here we are"
        print self.nameCache[className]
    def toClassName(self,obj):
        return obj.__class__.__name__
    def write(self,output,obj):
        self.nameCache[obj.getJavaClassName] = self.toClassName(obj)
        output.writeUTF(obj.getJavaClassName())
        obj.writeData(output)