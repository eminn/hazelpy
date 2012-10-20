from hazelpy.HazelcastClient import HazelcastClient
import unittest
class GeneralTest(unittest.TestCase):
	
	def setUp(self):
		self.hc = HazelcastClient("localhost",5701)

	def test_01_instances(self):
		print self.hc.instances()
	
	def test_02_members(self):
		print self.hc.members()
	
	def test_03_destroy(self):
		assert self.hc.destroy("map","mymap") == True , "destroy failed" 
	
	def test_04_ping(self):
		assert self.hc.ping() == True, "ping failed"
	
	def test_05_clusterTime(self):
		print self.hc.clusterTime()
	
	def test_06_partitions(self):
		self.hc.getMap("default").put("partitionTest","someValue")
		print self.hc.partitions("partitionTest")
		print self.hc.partitions()
	
	def tearDown(self):
		self.hc.close()