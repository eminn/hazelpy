from src.HazelcastClient import HazelcastClient
import unittest
class GeneralTest(unittest.TestCase):
	def setUp(self):
		self.hc = HazelcastClient("localhost")

	def test_01_instances(self):
		print self.hc.instances()
	def test_02_members(self):
		print self.hc.members()
	def test_03_destroy(self):
		assert self.hc.destroy("map","mymap") == True , "destroy failed" 
	def test_04_ping(self):
		assert self.hc.ping() == True, "ping failed"
	def tearDown(self):
		self.hc.close()