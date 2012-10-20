from hazelpy.HazelcastClient import HazelcastClient
import unittest

class QueueTest(unittest.TestCase):
	def setUp(self):
		self.hc = HazelcastClient("localhost",5701)
		self.queue = self.hc.getQueue("myqueue")
	def test_01_offer(self):
		assert self.queue.offer(11) == True , "offer failed"
	def test_02_peek(self):
		assert self.queue.peek() == 11 , "peek failed"
	def test_03_entries(self):
		entries =  self.queue.entries()
		self.queue.offer(145)
		entries.append(145)
		assert self.queue.entries() == entries, "retrieving entries failed"
		self.queue.remove(145)
		entries.remove(145)
		assert sorted(self.queue.entries()) == sorted(entries) , "retrieving entries failed"
	def test_04_size(self):
		size = self.queue.size()
		self.queue.offer(1)
		assert self.queue.size() == size + 1 , "size is wrong"
		self.queue.remove(1)
		assert self.queue.size() == size , "size is wrong"
	def test_05_take(self):
		self.queue.offer(21)
		assert	self.queue.take() == 21 , "take failed"
	def test_06_poll(self):
		assert self.queue.poll() == 11, "poll failed"
	def test_07_remove(self):
		self.queue.offer(123)
		assert self.queue.remove(123) == True, "remove failed"
	def test_08_remainingCapacity(self):
		remcap = self.queue.remainingCapacity()
		self.queue.offer(123)
		assert self.queue.remainingCapacity() == remcap -1 , "retrieving remcap failed" 
	def tearDown(self):
		self.hc.close()
