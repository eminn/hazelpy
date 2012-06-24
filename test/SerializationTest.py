import unittest
from DefaultSerializer import DefaultSerializer
from AbstractSerializer import AbstractSerializer
from DataSerializer import DataSerializer

class SerializationTest(unittest.TestCase):
    def setUp(self):
        self.serializer = AbstractSerializer(DataSerializer(), DefaultSerializer())
    def testIntegerSerializer(self):
        ba = bytearray()
        ba.extend([1, 2, 0, 0, 0, 121])
        assert self.serializer.toByte(121) == ba , "serialization error"
        assert self.serializer.toObject(ba) == 121 , "de-serialization error"
    
