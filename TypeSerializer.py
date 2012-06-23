from abc import ABCMeta ,abstractmethod
class TypeSerializer:
    __metaclass__ = ABCMeta
    @abstractmethod
    def priority(self):
        pass
    @abstractmethod
    def isSuitable(self):
        pass
    @abstractmethod
    def getTypeId(self):
        pass
    @abstractmethod
    def write(self):
        pass
    @abstractmethod
    def read(self):
        pass
    def __cmp__(self,other):
        return cmp(self.priority(),other.priority())