import unittest


def is_positive(number):
    return number > 0


class TestIsPositive(unittest.TestCase):
    def test_positive_number(self):
        result = is_positive(5)
        self.assertTrue(result, "5 is a positive number")

    def test_negative_number(self):
        result = is_positive(-5)
        self.assertFalse(result, "-5 is not a positive number")


if __name__ == '__main__':
    unittest.main()
