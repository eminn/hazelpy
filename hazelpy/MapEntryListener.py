from abc import ABCMeta, abstractmethod
from EntryListener import EntryListener
import ListenerManager
class MapEntryListener(EntryListener):
    TYPE_LISTENER = "map"
    listenerManager = None
    key = None
    name = None
    def __init__(self):
        __metaclass__ = ABCMeta
    @abstractmethod
    def entryAdded(self, event):
        raise NotImplementedError
    @abstractmethod
    def entryRemoved(self, event):
        raise NotImplementedError
    @abstractmethod
    def entryUpdated(self, event):
        raise NotImplementedError
    @abstractmethod
    def entryEvicted(self, event):
        raise NotImplementedError
    def removeThis(self):
        self.listenerManager.removeListenerOp(self,self.key,self.name)        