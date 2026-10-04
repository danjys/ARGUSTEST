import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_ac1_greet_argus_returns_hi_argus(self):
        """AC1: greet("ARGUS") returns "Hi, ARGUS"."""
        self.assertEqual(greet("ARGUS"), "Hi, ARGUS")


if __name__ == "__main__":
    unittest.main()
