# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient

hc = HazelcastClient()
hc.getMap("mymap").put(131, 52)
print "result of get"
entries = {21:3 , 3:4, "afaçç":"ss.ç"}
print hc.getMap("mymap").putAll(entries)
print hc.getMap("mymap").get("afaçç")
