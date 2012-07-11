from src.HazelcastClient import HazelcastClient
import unittest

class MapTest(unittest.TestCase):
    def setUp(self):
        self.hc = HazelcastClient("localhost",5702)
        self.map = self.hc.getMap("mymap")
    def testPutandUpdate(self):
     #   assert self.map.put(112, 24) == True ,"put error"
        assert self.map.put(112, 24) == 24 ,"update error"
    def testGet(self):
    	assert self.map.get(112) == 24 ,"get error"
