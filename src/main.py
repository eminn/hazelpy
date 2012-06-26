# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient

hc = HazelcastClient()
#print hc.getMap("mymap").put(1,"afsa")
#print hc.getMap("mymap").put(32,"afsa")
#print hc.getMap("mymap").put(14L,"afsa")
#
#print hc.getMap("mymap").put("eminn","afsssa")
#
#print hc.getMap("mymap").keySet()

print hc.getMap("mymap").evict(1)