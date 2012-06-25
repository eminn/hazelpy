# -*- coding: utf8 -*-

from HazelcastClient import HazelcastClient

hc = HazelcastClient()

print hc.getMap("mymap").get(2)
