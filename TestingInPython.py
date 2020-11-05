
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


