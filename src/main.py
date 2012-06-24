# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient

hc = HazelcastClient()
hc.getMap("mymap").put(131, 52)
print "result of get"
print hc.getMap("mymap").get(131)