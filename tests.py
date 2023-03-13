import unittest
from task import my_datetime, is_leap, numLeaps, findMo, conv_endian, dec_to_hex, conv_num

class TestConvNum(unittest.TestCase):
    def test_conv_num(self):
        test_cases = [
            ('12345', 12345),
            ('-123.45', -123.45),
            ('.45', 0.45),
            ('123.', 123.0),
            ('0xAD4', 2772),
            ('0xAZ4', None),
            ('12345A', None),
            ('12.3.45', None),
        ]
        for num_str, expected_result in test_cases:
            result = conv_num(num_str)
            self.assertEqual(result, expected_result)


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    # --- testing my_datetime function --- #
    def test2(self):
        # Checks that returned value is a string
        self.assertIsInstance(my_datetime(0), str)

    def test3(self):
        # verifies that the epoch is returned correctly
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test4(self):
        # verify is_leap helper returns True correctly
        self.assertTrue(is_leap(1976))

    def test5(self):
        # verify is_leap helper returns False correctly
        self.assertFalse(is_leap(1974))

    def test6(self):
        # verify numLeaps helper returns correct integer
        self.assertEqual(numLeaps(2000), 8)

    def test7(self):
        # verify numLeaps helper returns correct integer when very large
        self.assertEqual(numLeaps(8360), 1550)

    def test8(self):
        # verify findMo helper returns correct tuple
        self.assertEqual(findMo(False, 35), (4, 1))

    def test9(self):
        # verify my_datetime() output matches assignment sample
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test10(self):
        # verify my_datetime() output matches assignment sample
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    def test11(self):
        # verify my_datetime() output matches assignment sample
        self.assertEqual(my_datetime(201653971200), "02-29-8360")

    def test12(self):
        # verify my_datetime() returns correctly on NYE when leap year
        self.assertEqual(my_datetime(9687991520), "12-31-2276")

    # --- end of my_datetime() testing --- #

    # --- testing conv_endian() function --- #
    def test13(self):
        # Verify dec_to_hex converts to hex properly
        self.assertEqual(dec_to_hex(954786), ["E", 9, 1, "A", 2])

    def test14(self):
        # Verify conv_endian returns big endian with no second argument
        self.assertEqual(conv_endian(954786), "0E 91 A2")

    def test15(self):
        # Verify conv_endian returns negative values properly
        self.assertEqual(conv_endian(-954786), "-0E 91 A2")

    def test16(self):
        # Verify conv_endian returns little endian properly
        self.assertEqual(conv_endian(954786, "little"), "A2 91 0E")

    def test17(self):
        # Verify conv_endian returns negative little endian properly
        self.assertEqual(conv_endian(-954786, "little"), "-A2 91 0E")

    def test18(self):
        # Verify conv_endian returns invalid endian properly
        self.assertEqual(conv_endian(-954786, "small"), None)

    def test19(self):
        # Verify conv_endian returns even length hex value correctly
        self.assertEqual(conv_endian(2959261, "big"), "2D 27 9D")

    def test20(self):
        # Verify conv_endian returns invalid endian properly
        self.assertEqual(conv_endian(2959261, ""), None)

    def test21(self):
        # Verify conv_endian returns num = 1 properly
        self.assertEqual(conv_endian(1, "big"), "01")

    def test22(self):
        # Verify conv_endian returns num = 0 properly
        self.assertEqual(conv_endian(0, "little"), "00")

    # --- end of conv_endian() testing --- #


if __name__ == '__main__':
    unittest.main(verbosity=2)

