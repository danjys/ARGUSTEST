import unittest

from hello import hello


class TestHello(unittest.TestCase):
    def test_ac1_hello_argus_returns_greeting(self):
        """AC1: hello("ARGUS") returns "Hello, ARGUS!"."""
        self.assertEqual(hello("ARGUS"), "Hello, ARGUS!")


if __name__ == "__main__":
    unittest.main()
