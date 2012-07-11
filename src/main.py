# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient
from MapEntryListener import MapEntryListener
from DataSerializable import DataSerializable
import threading
class el(MapEntryListener):
    def entryAdded(self,event):
        print "entry Added"
        print "key->" , event.key
        print "value->" , event.value
    def entryRemoved(self, event):
        print "entry rm"
        print "key->" , event.key
        print "value->" , event.value
        self.removeThis()
    def entryUpdated(self,event):
        print "entry up"
        print "key->" , event.key
        print "value->" , event.value
        print "oldValue->" , event.oldValue
    def entryEvicted(self, event):
        print "entry evi"
        print "key->" , event.key

class t(threading.Thread):
    def run(self):
        client = HazelcastClient()
        mymap = client.getMap("mymap")
        els = el()
        mymap.addListener(els,None,True)
t().start()

class Person(DataSerializable):
    def __init__(self):
        self.name = "emin"
        self.surname = "demirci"
        self.javaClassName = "com.eminn.Person"
    def readData(self,inputStream):
        self.name = inputStream.readUTF()
        self.surname = inputStream.readUTF()
    def writeData(self,outputStream):
        outputStream.writeUTF(self.name)
        outputStream.writeUTF(self.surname)
    def getJavaClassName(self):
        return self.javaClassName

person = Person()
hc = HazelcastClient("localhost",5702)
mymap = hc.getMap("mymap")
#mymap.put(1,person)
print mymap.get(2)
mymap.remove(21)

myqueue = hc.getQueue("myqueue")
myqueue.offer(1)