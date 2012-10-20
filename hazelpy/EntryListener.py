from abc import ABCMeta, abstractmethod
class EntryListener:
    __metaclass__ = ABCMeta
    @abstractmethod
    def entryAdded(self,event):
        raise NotImplementedError
    @abstractmethod
    def entryRemoved(self,event):
        raise NotImplementedError
    @abstractmethod
    def entryUpdated(self,event):
        raise NotImplementedError
    @abstractmethod
    def entryEvicted(self,event):
        raise NotImplementedError
