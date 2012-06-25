# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient

hc = HazelcastClient()
hc.getMap("mymap").put(131, 52)
print "result of get"
print hc.getMap("mymap").get(5)
entries = {21:3 , 3:4, 5:"ss6"}
print hc.getMap("mymap").putAll(entries)
