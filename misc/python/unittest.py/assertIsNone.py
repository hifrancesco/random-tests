import unittest

def return_none():
    return None

class TestReturnNone(unittest.TestCase):
    def test_return_none(self):
        result = return_none()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
