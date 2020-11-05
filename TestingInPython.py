
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





# MORE TEST CONCEPTS IN PYTHON

# Black and White Boxes
# white box testing ("CLear Box testing/ Transparent testing")
# Relies mainly on creator's knowledge of the s/w being tested to construct a test

# Black boxes, the user has now idea of how the test is working
# written with awareness of what the program is supposed to do-->its requirements/specification
# but not how it does


# Intergration Test
# Verify interactions with different platforms like server and cLient side
# Regression test----> used to check if the written program has been corrected from the error
# smoke test/Build verification test---->test hardware
# Load test---> check if system is behaving well under certain load work force




# Test Driven Development (TDD)
# create test before writing code
# check continuos integration



# Errors and Exception
# Try Except Construct

# Count the frequency of each character in a file
def character_sequence(filename):
    try:
        f = open(filename)
    except OSError:
        return None
    # Go through the files by processing each character
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char,0) + 1
    f.close()
    return characters


# Raising Errors where need be
# working with usernames and validation
def validate_user(username, minlen):
    if len(username)< minlen:
        return False
    if not username.isalnum():
        return False
    return True
# this is not always the case bacause some could have upto one char name , so let's check the soln
def validate_user(username, minlen):
    if minlenM < 1:
        raise ValueError("minimum Len must atleast  be 1 char")
    if len(username)< minlen:
        return False
    if not username.isalnum():
        return False
    return True


# add assertion to cath more errors to handle non-string inputs
def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlenM < 1:
        raise ValueError("minimum Len must atleast  be 1 char")
    if len(username)< minlen:
        return False
    if not username.isalnum():
        return False
    return True




# Testing for expected Errors
# using unit test

import unittest
from validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("valid_user",3), True)
    def test_too_short(self):
        self.assertEqual(validate_user("INV",5), False)
    def test_invalid_characters(self):
        self.assertEqual(validate_user("Invalid_user",1), False)
    #now implement the assert Raise
    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user,"User", -1)
#Run the test now
unittest.main()




