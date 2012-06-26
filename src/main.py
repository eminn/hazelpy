# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient
import time

hc = HazelcastClient()
keys =  hc.getMap("mymap").keySet()
print len(keys)

values = []
for key in keys:
    print "key-> " + str(key) + ",value-> " + str(hc.getMap("mymap").get(key))
print len(keys)

hc.close()  