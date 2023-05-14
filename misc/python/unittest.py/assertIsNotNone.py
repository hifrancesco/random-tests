import unittest

def return_not_none():
    return "some value"

class TestReturnNotNone(unittest.TestCase):
    def test_return_not_none(self):
        result = return_not_none()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
