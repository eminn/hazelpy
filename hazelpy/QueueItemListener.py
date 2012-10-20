from abc import ABCMeta, abstractmethod
from ItemListener import ItemListener
import ListenerManager
class QueueItemListener(ItemListener):
    TYPE_LISTENER = "queue"
    listenerManager = None
    name = None
    def __init__(self):
        __metaclass__ = ABCMeta
    @abstractmethod
    def itemAdded(self,event):
        raise NotImplementedError
    @abstractmethod    
    def itemRemoved(self,event):
        raise NotImplementedError
    def removeThis(self):
        self.listenerManager.removeListenerOp(self,self.name)