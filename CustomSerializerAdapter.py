from TypeSerializer import TypeSerializer
class CustomSerializerAdapter(TypeSerializer):
    def __init__(self,serializer):
        self.serializer = serializer
    def write(self,output,object):
        self.serializer.write(output,object)
    def read(self,input):
        raise NotImplementedError
    def priority(self):
        return 100
    def isSuitable(self,object):
        return True
    def getTypeId(self):
        return 1
