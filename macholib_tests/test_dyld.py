from macholib import dyld

import unittest


class TestDyld (unittest.TestCase):
    def test_missing(self):
        self.fail("tests are missing")

if __name__ == "__main__":
    unittest.main()