from src.HazelcastClient import HazelcastClient
import unittest

class MapTest(unittest.TestCase):
    def setUp(self):
        self.hc = HazelcastClient("localhost")
        self.map = self.hc.getMap("mymap")
    def test_01_put(self):
    	result = self.map.put(12,12)
    	assert (result in [True,12]) == True, "put failed"
    def test_02_get(self):
    	assert self.map.get(12) == 12 ,"get failed"
    def test_03_set(self):
    	self.map.set(12,13)
    	assert self.map.get(12) == 13 , "set failed"
    def test_04_containsKey(self):
    	assert self.map.containsKey(12) == True , "conatinsKey failed"
    def test_05_containsValue(self):
    	assert self.map.containsValue(13) == True , "conatinsValue failed"
    def test_06_keySet(self):
    	self.map.put(13,14)
    	self.map.put(14,15)
    	assert set([13,14]).issubset(self.map.keySet())  == True , "retrieving keySet failed"
    def test_07_getAll(self):
    	assert set([13,14,15]).issubset(self.map.getAll(self.map.keySet())) == True, "getAll failed"
    def test_08_putAll(self):
    	y={}
    	for x in range(1,4):
  			y[x]=x
       	print y,self.map.keySet()
    	self.map.putAll(y)
    	assert set(y.keys()).issubset(self.map.keySet())  == True, "putAll failed" 
    def test_11_Remove(self):
    	assert self.map.remove(12) == 13 , "remove failed"

