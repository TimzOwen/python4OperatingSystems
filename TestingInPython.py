
 # Software Testing

# The process of evaluating computer code to determine wether or not it does what you want

# Manual and Automated Testing Code
# Manual testing is writing code and executing to check form the same script
# automatic testing-Writing code to check the code with test cases

# UNIT TESTING IN PYTHON
# Used to verify the small, isolated parts of a program are correct. Only test target isolated code

# rearage user names
import re
from rearrange import rearrange_name
def rearrange_name(name):
    results = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {} ".format(results[2], results[1])
#now import the reaarange and run the unit test
print(rearrange_name("Lovelace, Ave"))


# Writing Automated Tasks test:
# check the _test file on the main repo where we test the code and run it

# Edge Cases
# This are inputs to our code that produces unexpected results and are found at the extreme
# ends of the ranges of the input we imagine our program will typically work with

# check for the unit test file as it continues to debug and test there

# Fix the errors and run the test file by adding if None return an empty string


import re
from rearrange import rearrange_name
def rearrange_name(name):
    results = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if results in None:
        return ""
    return "{} {} ".format(results[2], results[1])
#now import the reaarange and run the unit test
print(rearrange_name("Lovelace, Ave"))




# Test case with one user name corrected by not returning null

import re
from rearrange import rearrange_name
def rearrange_name(name):
    results = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if results in None:
        return name  # otherwise if the result id "" , throws an error
    return "{} {} ".format(results[2], results[1])
#now import the reaarange and run the unit test
print(rearrange_name("Lovelace, Ave"))




# MORE EXAMPLES AND EXCISES
# unit test and edge cases test


# Letter compile character
import re

my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt)) # ['a','b']
# Now use unit test to check for the test
import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)
unittest.main(argv = ['first-arg-is-ignored'], exit = False)

#Now add more test cases
class TestCompiler2(unittest.TestCase):

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
unittest.main(argv = ['first-arg-is-ignored'], exit = False) # NOW THE code has more compilations


