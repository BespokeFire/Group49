import unittest
from task import my_datetime, is_leap, numLeaps, findMo


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    # --- testing my_datetime function --- #
    def test2(self):
        # Checks that returned value is a string
        self.assertIsInstance(my_datetime(0), str)

    def test3(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test4(self):
        self.assertTrue(is_leap(1976))

    def test5(self):
        self.assertFalse(is_leap(1974))

    def test6(self):
        self.assertEqual(numLeaps(2000), 8)

    def test7(self):
        self.assertEqual(numLeaps(8360), 1550)

    def test8(self):
        self.assertEqual(findMo(False, 35), (4, 1))


if __name__ == '__main__':
    unittest.main()
