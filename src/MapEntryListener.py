from abc import ABCMeta, abstractmethod
from EntryListener import EntryListener
class MapEntryListener(EntryListener):
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
