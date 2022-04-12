
import unittest
from file_controller import file_controller

from file_controller import file_controller

class testLoad(unittest.TestCase):
    def test_method_load(self):
        load = file_controller()
        file = "prove.txt"
        self.assertEqual(load.load(file) ,"No file found")
        self.assertEqual(load.loadLine(file=None), "No file found")
        self

if __name__ == 'main':
    unittest.main()

