import unittest
import cotu


class TestHW(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(cotu.hello_world(), "hello world")

if __name__ == '__main__':
    unittest.main()
