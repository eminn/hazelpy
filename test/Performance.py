from PerformanceTest import PerformanceTest
import unittest,threading
class Perfomance:
	finished = threading.Event()
	def __init__(self):
		unittest.TestLoader().loadTestsFromTestCase(PerformanceTest)
		unittest.main(verbosity=2)
		finished.wait()
Perfomance()
