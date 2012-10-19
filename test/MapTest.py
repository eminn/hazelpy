from src.HazelcastClient import HazelcastClient
from src.MapEntryListener import MapEntryListener
import unittest,threading,time

class MapTest(unittest.TestCase):
    
    def setUp(self):
        self.hc = HazelcastClient("localhost",5701)
        self.map = self.hc.getMap("mymap")
    
    def test_01_put(self):
    	result = self.map.put(1,111)
    	assert (result in [True,111]) == True, "put failed"
    
    def test_02_get(self):
        value = self.map.get(1)
    	assert  value == 111 ,"get failed"
    
    def test_03_set(self):
    	self.map.set(12,13)
        value = self.map.get(12)
    	assert  value == 13 , "set failed"
    
    def test_04_containsKey(self):
        result = self.map.containsKey(12)
    	assert  result == True , "conatinsKey failed"
    
    def test_05_containsValue(self):
        result = self.map.containsValue(13)
    	assert  result == True , "conatinsValue failed"
    
    def test_06_keySet(self):
    	self.map.put(13,14)
    	self.map.put(14,15)
        result = self.map.keySet()
    	assert set([13,14]).issubset(result)  == True , "retrieving keySet failed"
    
    def test_07_getAll(self):
    	assert set([13,14,15]).issubset(self.map.getAll(self.map.keySet()).values()) == True, "getAll failed"
    
    def test_08_putAll(self):
    	y={}
    	for x in range(1,4):
  			y[x]=x
    	self.map.putAll(y)
    	assert set(y.keys()).issubset(self.map.keySet())  == True, "putAll failed" 
    
    def test_09_evict(self):
        self.map.put("evictTest", "someValue")
        assert self.map.evict("evictTest") == True , "evict failed"
        assert self.map.containsKey("evictTest") == False , "evicted key still in map"

    def test_10_putTransient(self):
        result = self.map.put(66,66)
        assert (result in [True,66]) == True, "putTransient failed"
    
    def test_11_remove(self):
    	assert self.map.remove(12) == 13 , "remove failed"
    
    def test_12_mapSize(self):
        self.map.put("testRemove","someValue")
        current = self.map.size()
        self.map.remove("testRemove")
        next = self.map.size()
        assert next == current - 1, "size failed"
    
    def test_13_tryPut(self):
        result = self.map.tryPut("ali","veli",5);
        assert result == True , "tryPut failed"
    
    def test_14_lock(self):
        self.map.lock(14)
        result = self.map.isKeyLocked(14)
        assert result == True , "lock failed"

    def test_15_unlock(self):
        self.map.lock(555)
        self.map.unLock(555)
        assert self.map.isKeyLocked(555) == False, "unlock failed"
        
    def test_16_putAndUnlock(self):
        self.map.put("testPutAndUnlock","someValue")
        self.map.lock("testPutAndUnlock")
        assert self.map.putAndUnlock("testPutAndUnlock","updatedValue") == True , "putAndUnlock failed"
    
    def test_17_tryLockAndGet(self):
        self.map.put("testTryLockAndGet" , "someValue")
        result = self.map.tryLockAndGet( "testTryLockAndGet" , 5)
        assert result == "someValue" and self.map.isKeyLocked("testTryLockAndGet"), "tryLockAndGet failed"

    def test_18_tryRemove(self):
        self.map.put("tryRemove","someValue")
        assert self.map.tryRemove("tryRemove",5) == "someValue" , "tryRemove failed"
    
    def test_19_forceUnlock(self):
        self.map.put("forceUnlock","someValue")
        self.map.lock("forceUnlock")
        assert self.map.forceUnlock("forceUnlock") == True , "forceUnlock failed"

    def test_20_removeIfSame(self):
        self.map.put("removeIfSame","someValue")
        assert self.map.removeIfSame("removeIfSame","someValue") == True , "removeIfSame failed"
        assert self.map.containsKey("removeIfSame") == False  , "removeIfSame failed"

    def test_21_tryLock(self):
        self.map.put("tryLock", "someValue")
        assert self.map.tryLock("tryLock",5) == True , "tryLock failed"
        assert self.map.isKeyLocked("tryLock") == True, "tryLock failed"

    def test_22_putIfAbsent(self):
        self.map.putIfAbsent("putIfAbsent","someValue")
        assert self.map.get("putIfAbsent") == "someValue", "putIfAbsent failed"

    def test_23_lockMap(self):
        self.map.put("lockMap","someValue")
        assert self.map.lockMap(5) == True ,"lockMap failed"

    def test_24_flush(self):
        assert self.map.flush() == True, "flushing failed"
    
    def test_25_addListener(self):
        return
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

        hc = HazelcastClient()
        listener = MapListener()
        mymap = hc.getMap(listenedMapName)
        mymap.addListener(listener,None,True)
        self.hc.getMap(listenedMapName).put(1,1)
        self.hc.getMap(listenedMapName).put(1,2)
        self.hc.getMap(listenedMapName).remove(1)
        self.hc.getMap(listenedMapName).put(1,1)
        self.hc.getMap(listenedMapName).evict(1)
        mymap.removeListener(listener)


    def tearDown(self):
    	self.hc.close()
