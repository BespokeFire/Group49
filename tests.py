import unittest
from task import my_datetime 

class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test2(self):
        # Checks that returned value is a string
        self.assertIsInstance(my_datetime(0), str)

if __name__ == '__main__':
    unittest.main()
