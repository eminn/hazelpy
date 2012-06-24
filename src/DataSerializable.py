from abc import ABCMeta, abstractmethod
class DataSerializable:
    __metaclass__ = ABCMeta
    @abstractmethod
    def writeData(self,output):
        raise NotImplementedError
    @abstractmethod
    def readData(self,inputStream):
        raise NotImplementedError
