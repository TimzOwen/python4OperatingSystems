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

#!usr/bin/env python3


# Testing when given an empty string to check for the error


from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Loveace, Ada"
        expected = "Ada Loveace"
        self.assertAlmostEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
# to run call the unit main test
unittest.main()

# save and execute the code



# TEST FOR MORE CASES more than one Name

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Loveace, Ada"
        expected = "Ada Loveace"
        self.assertAlmostEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
# to run call the unit main test
unittest.main()

# save and execute the code



# Test Case for one user
# remember to change the return empty otherwise returns an errors on the main code

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Loveace, Ada"
        expected = "Ada Loveace"
        self.assertAlmostEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Owen"
        expected = "Owen"
        self.assertAlmostEqual(rearrange_name(testcase), expected)
# to run call the unit main test
unittest.main()
