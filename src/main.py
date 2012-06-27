# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient
from MapEntryListener import MapEntryListener

hc = HazelcastClient()
keys =  hc.getMap("mymap").keySet()
print keys
class el(MapEntryListener):
    def entryAdded(self,event):
        print "entry Adsded"
    def entryRemoved(self, event):
        print "entry rm"
    def entryUpdated(self,event):
        print "entry up"
    def entryEvicted(self, event):
        print "entry evi"

hc.getMap("mymap").addListener(el())
hc.getMap("default").addListener(el())

hc.getMap("mymap").put(21,1222)
values = []
for key in keys:
    print "key-> " + str(key) + ",value-> " + str(hc.getMap("mymap").get(key))
print len(keys)

hc.close()  