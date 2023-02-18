import unittest


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b


class TestDivide(unittest.TestCase):
    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertEqual(str(context.exception), "division by zero")


if __name__ == '__main__':
    unittest.main()
