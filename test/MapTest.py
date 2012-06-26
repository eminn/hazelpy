from src.HazelcastClient import HazelcastClient
import unittest

class MapTest(unittest.TestCase):
    def setUp(self):
        self.hc = HazelcastClient()
        self.map = self.hc.getMap("mymap")
    def testPutandGet(self):
        assert self.map.put(112, 24) == 24 ,"put error"
        assert self.map.get(112) == 24 ,"get error"