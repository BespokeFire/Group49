import unittest
from task import my_datetime 

class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)
    # --- testing my_datetime function --- #
    def test2(self):
        # Checks that returned value is a string
        self.assertIsInstance(my_datetime(0), str)
        
    def test3(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

if __name__ == '__main__':
    unittest.main()
