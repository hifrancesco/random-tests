import unittest

def get_type(value):
    return type(value)

class TestGetType(unittest.TestCase):
    def test_get_type(self):
        result = get_type(0)
        self.assertIsInstance(result, int)

if __name__ == '__main__':
    unittest.main()
