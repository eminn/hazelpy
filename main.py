# -*- coding: utf8 -*-

from Connection import Connection
from HazelcastClient import HazelcastClient

hc = HazelcastClient()
hc.getMap("mymap").put("öç", "hgfhfga")
hc.getMap("mymap").put("enşlçö", "hgfhfga")
hc.getMap("mymap").put("eminç", "hgfhfga")

hc.getMap("mymap").put(1221, 42)
hc.getMap("mymap").put(131, 52)
