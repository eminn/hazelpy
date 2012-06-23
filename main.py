from Connection import Connection
from HazelcastClient import HazelcastClient

hc = HazelcastClient()
hc.getMap("mymap").put(1, "atatat")

while True:
    pass