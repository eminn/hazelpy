from abc import ABCMeta, abstractmethod
class ItemListener:
    __metaclass__ = ABCMeta
    @abstractmethod
    def itemAdded(self,event):
        raise NotImplementedError
    @abstractmethod
    def itemRemoved(self,event):
        raise NotImplementedError