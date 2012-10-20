import unittest
from hazelpy.DefaultSerializer import DefaultSerializer
from hazelpy.AbstractSerializer import AbstractSerializer
from hazelpy.DataSerializer import DataSerializer
class person:
	def __init__(self,name,surname):
		self.name = name
		self.surname = surname
class SerializationTest(unittest.TestCase):
    def setUp(self):
        self.serializer = AbstractSerializer(DataSerializer(), DefaultSerializer())
    def test_01_integerSerialization(self):
        assert self.serializer.toByte(121) == [1, 2, 0, 0, 0, 121] ,"serialization error"
    def test_02_integerDeserialiation(self):    
    	assert self.serializer.toObject([1, 2, 0, 0, 0, 121]) == 121 , "de-serialization error"
    def test_03_bytearraySerialization(self):
    	data=self.serializer.toByte(person("emin","demirci"))
    	print data
    	obj = self.serializer.toObject(data)
        print obj