import unittest
from src.DefaultSerializer import DefaultSerializer
from src.AbstractSerializer import AbstractSerializer
from src.DataSerializer import DataSerializer

class SerializationTest(unittest.TestCase):
    def setUp(self):
        self.serializer = AbstractSerializer(DataSerializer(), DefaultSerializer())
    def testIntegerSerializer(self):
        assert self.serializer.toByte(121) == [1, 2, 0, 0, 0, 121] ,"serialization error"
        assert self.serializer.toObject([1, 2, 0, 0, 0, 121]) == 121 , "de-serialization error"
    
