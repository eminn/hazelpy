from TypeSerializer import TypeSerializer
class CustomSerializerAdapter(TypeSerializer):
    def __init__(self,serializer):
        self.serializer = serializer
    def write(self,output,obj):
        self.serializer.write(output,obj)
    def read(self,inputStream):
        return self.serializer.read(inputStream)
    def priority(self):
        return 100
    def isSuitable(self,obj):
        return True
    def getTypeId(self):
        return 1
