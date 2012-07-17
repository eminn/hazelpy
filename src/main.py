# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient
from DataSerializable import DataSerializable
from QueueItemListener import QueueItemListener
import threading
class el(QueueItemListener):
    def itemAdded(self,event):
        print "entry Added"
        print "key->" , event.key
        print "value->" , event.value
    def itemRemoved(self, event):
        print "entry rm"
        print "key->" , event.key
        print "value->" , event.value
        self.removeThis()

class t(threading.Thread):
    def run(self):
        client = HazelcastClient("localhost",5701)
        mymap = client.getQueue("myqueue")
        els = el()
        mymap.addListener(els)
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
hc = HazelcastClient("localhost",5701)
mymap = hc.getMap("mymap")
#mymap.put(1,person)
mymap.put(21,214)
mymap.put(212,441)
mymap.put(21,"as")
mymap.remove(212)
mymap.remove(21)
myqueue = hc.getQueue("myqueue")
myqueue.offer(1)