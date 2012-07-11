from src.HazelcastClient import HazelcastClient
import unittest

class QueueTest(unittest.TestCase):
	def setUp(self):
		self.hc = HazelcastClient("localhost",5702)
		self.queue = self.hc.getQueue("myqueue")
	def test_01_offer(self):
		assert self.queue.offer(11) == True , "offer failed"
	def test_02_peek(self):
		assert self.queue.peek() == 11 , "peek failed"
	def test_03_size(self):
		assert self.queue.size() == 1 , "size is wrong"
	def test_04_take(self):
		self.queue.offer(21)
		assert	self.queue.take() == 21 , "take failed"
	def test_05_poll(self):
		assert self.queue.poll() == 11, "poll failed"
	def test_06_remove(self):
		self.queue.offer(123)
		assert self.queue.remove(123) == True, "remove failed"
	def test_07_remainingCapacity(self):
		remcap = self.queue.remainingCapacity()
		self.queue.offer(123)
		assert self.queue.remainingCapacity() == remcap -1 , "retrieving remcap failed" 

