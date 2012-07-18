from src.HazelcastClient import HazelcastClient
from src.MapEntryListener import MapEntryListener
import unittest,threading,time

class MapTest(unittest.TestCase):
    def setUp(self):
        self.hc = HazelcastClient("localhost",5702)
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
    	self.map.putAll(y)
    	assert set(y.keys()).issubset(self.map.keySet())  == True, "putAll failed" 
    def test_09_addListener(self):
        listenedMapName = "listenerTest1"
        class MapListener(MapEntryListener):
            def entryAdded(self,event):
                print "entry added"
                print "key->" , event.key
                print "value->" , event.value
                assert event.key == 1 , "key is wrong"
                assert event.value == 1, "value is wrong"
            def entryRemoved(self, event):
                print "entry removed"
                print "key->" , event.key
                print "value->" , event.value
                assert event.key == 1 , "key is wrong"
                assert event.value == 2, "value is wrong"
            def entryUpdated(self,event):
                print "entry updated"
                print "key->" , event.key
                print "value->" , event.value
                print "oldValue->" , event.oldValue
                assert event.key == 1 , "key is wrong"
                assert event.value == 2, "value is wrong"
                assert event.oldValue == 1, "oldValue is wrong"
            def entryEvicted(self, event):
                print "entry evicted"
                print "key->" , event.key
                assert event.key == 1 , "key is wrong"
                done.set()
        class ListenerThread(threading.Thread):
            def run(self):
                hc = HazelcastClient()
                mymap = hc.getMap(listenedMapName)
                mymap.addListener(MapListener(),None,True)
        lt = ListenerThread()
        lt.start()
        time.sleep(2)
        done = threading.Event()
        self.hc.getMap(listenedMapName).put(1,1)
        self.hc.getMap(listenedMapName).put(1,2)
        self.hc.getMap(listenedMapName).remove(1)
        self.hc.getMap(listenedMapName).put(1,1)
        self.hc.getMap(listenedMapName).evict(1)
        done.wait()

    def test_11_Remove(self):
    	assert self.map.remove(12) == 13 , "remove failed"
    def tearDown(self):
    	self.hc.close()
