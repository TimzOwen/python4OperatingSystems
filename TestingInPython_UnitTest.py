#!usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Loveace, Ada"
        expected = "Ada Loveace"
        self.assertAlmostEqual(rearrange_name(testcase), expected)
# to run call the unit main test
unittest.main()

# save and execute the code
