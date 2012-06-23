from OutputStream import OutputStream
from CustomSerializerAdapter import CustomSerializerAdapter
class AbstractSerializer:
    def __init__(self,ds,cs):
        self.ds = ds
        self.cs = CustomSerializerAdapter(cs)
        self.output = OutputStream()
        #self.input = InputStream()
    def toByte(self,object):
        self.output.flush()
        if object == None:
            return
        ts = self.ds if self.ds.isSuitable(object) else self.cs
        self.output.writeByte(ts.getTypeId())
        ts.write(self.output,object)
        return self.output.buf

