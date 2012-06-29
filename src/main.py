# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient
from MapEntryListener import MapEntryListener

hc = HazelcastClient()
class el(MapEntryListener):
    def entryAdded(self,event):
        print "entry Adsded"
        print "key->" , event.key
        print "value->" , event.value
    def entryRemoved(self, event):
        print "entry rm"
        print "key->" , event.key
        print "value->" , event.value

    def entryUpdated(self,event):
        print "entry up"
        print "key->" , event.key
        print "value->" , event.value
        print "oldValue->" , event.oldValue
    def entryEvicted(self, event):
        print "entry evi"
        print "key->" , event.key
el = el()
hc.getMap("mymap").addListener(el,21,True)

hc.getMap("mymap").put(212,122)
hc.getMap("mymap").put(212,122)
hc.getMap("mymap").put(21,1222)

hc.getMap("mymap").remove(21)
