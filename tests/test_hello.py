import os
import subprocess
import sys
import unittest

from hello import hello

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHILD_RUN_ENV = "HELLO_AC2_CHILD_RUN"


class TestHello(unittest.TestCase):
    def test_ac1_hello_argus_returns_greeting(self):
        """AC1: hello("ARGUS") returns "Hello, ARGUS!"."""
        self.assertEqual(hello("ARGUS"), "Hello, ARGUS!")

    @unittest.skipIf(os.environ.get(CHILD_RUN_ENV), "inside the AC2 child run")
    def test_ac2_unittest_discover_passes(self):
        """AC2: python -m unittest discover -s tests passes."""
        env = dict(os.environ, **{CHILD_RUN_ENV: "1", "PYTHONDONTWRITEBYTECODE": "1"})
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
            cwd=REPO_ROOT,
            env=env,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
