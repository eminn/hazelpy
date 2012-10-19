from src.HazelcastClient import HazelcastClient
import unittest,threading,random,time
class PerformanceTest(unittest.TestCase):
	lock  = threading.Lock()	
	putOperationCount = 0
	getOperationCount = 0
	removeOperationCount = 0
	THREAD_COUNT = 1
	ENTRY_COUNT = 10 * 1000
	VALUE_SIZE = 10000
	GET_PERCENTAGE = 80
	PUT_PERCENTAGE = 20
	counter = 1
	def setUp(self):
		pass
	def test_01_performance(self):
		class ClientThread(threading.Thread):
			def run(self):
				hc = HazelcastClient("localhost",5701)
				mymap = hc.getMap("default")
				while True:
					key = int(random.random() * PerformanceTest.ENTRY_COUNT)
					operation = int(random.random() * 100)
					if operation < PerformanceTest.GET_PERCENTAGE:
						mymap.get(key)
						PerformanceTest.getOperationCount +=1
					elif operation < PerformanceTest.GET_PERCENTAGE + PerformanceTest.PUT_PERCENTAGE:
						mymap.put(key,"x" * PerformanceTest.VALUE_SIZE)
						PerformanceTest.putOperationCount +=1
					else:
						mymap.remove(key)
						PerformanceTest.removeOperationCount +=1
		for i in range(0,PerformanceTest.THREAD_COUNT):
			ClientThread().start()
		while PerformanceTest.counter<10:
			time.sleep(5)
			print "ops per second : " + str((PerformanceTest.putOperationCount + PerformanceTest.getOperationCount + PerformanceTest.removeOperationCount) / 5)
			PerformanceTest.putOperationCount = 0
			PerformanceTest.getOperationCount = 0
			PerformanceTest.removeOperationCount = 0
			PerformanceTest.counter += 1
