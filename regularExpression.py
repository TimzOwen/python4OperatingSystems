import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


vtxt = "The rain in Spain"
x = re.split("\s", txt)
print(x)




line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"
   
   
   >>> import re
>>> s = '(zyx)bc'
>>> print (re.findall(r'(?<=\()\w+(?=\))|\w', s))
['zyx', 'b', 'c']

(?<=\() // lookbehind for left parenthesis
\w+     // all characters until:
(?=\))  // lookahead for right parenthesis
|       // OR
\w      // any character

a = re.findall(r'\((.*?)\)|(.)', '(zyx)bc',re.DEBUG); a
[('zyx', ''), ('', 'b'), ('', 'c')]
branch 
  literal 40 
  subpattern 1 
    min_repeat 0 65535 
      any None 
  literal 41 
or
  subpattern 2 
    any None
      
      
      

#REGULAR EXPRESSION
import re
log = "July 31 07:51:48 my computer bad_process=[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

#example 2
#!/usr/bin/python
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter

#Basic matching with grep

grep  thon /user/share/file  #prints files with *thon

#.dot
grep l.rts /usr/shre/dict/words #[prints all words with the characters mentioned]

# ^ caret indicate start of a word
# $ dollar sign indicate end of a word

grep ^ fruit /user/share/dict/wordchars
grep cat$ /user/share/dict/word
      

   
#Simple matching
result = re.search(r"aza","plaza")
print(result)
<re.Match object; span=(2, 5), match='aza'>

#combine
print(re.search(r"^X","Xenon"))
<re.Match object; span=(0, 1), match='X'>

#matching char
print(re.search(r"p.ng","penguin"))
<re.Match object; span=(0, 4), match='peng'>

#check if text passed contains vowels
import re
def check_aei (text):
  result = re.search(r"a.e.i", text) #or ([aei]).\1
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

#no Case sensitive
print(re.search(r"p.ng","Pangae", re.IGNORECASE))
<re.Match object; span=(0, 4), match='Pang'>



#Wild cards and character classes 
#Wild cards and character classes
#wildcards can match more than one char
#char classes in square brackets allows users to search for specific char in string

import re 

print(re.search(r,"[Pp]ython",Python))

# match all lower case letter
print(re.search(r"[a-z]way","The end of the highway"))
print(re,search("cloud[a-zA-Z0-9", "cloudy"))



#  check if the text passed contains punctuation    
# symbols: commas, periods, colons, semicolons, question marks, and exclamation points.


import re
def check_punctuation (text):
  result = re.search(r".:;?!", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#search for any char not a letter
print(re.search(r,"[^a-zA-Z]","This is a super highway")) # detects spaces
print(re.search(r,"[^a-zA-Z ]","This is a super highway")) # detects fullstop because we added the space after Z

#pipe to macth certain words
print(re.search(r"cat|dog", "I like cats")) # returns True and match
print(re.search(r"cat|dog", "I like cats")) # Returns true again
print(re.search(r"cat|dog", "I like cats and dogs")) # returns first element alone
print(re.findall(r"cat|dog", "I like cats")) # returns both the cat and the dog


# Repetition qualifiers
# allows us to find all the matching words
import re

print(re.search(r"Py.*n","Pymalion")) # Pymalion
print(re.search(r"Py.*n","Python Programming")) # Python, Programin

print(re.search(r"Py[a-z]*n","Python programming")) #python as the only complete ,and not being Greedy

#egrep (+?)
print(re.search(r"o+l+","goldfish")) #match "ol"
print(re.search(r"o+l+","woolly")) # match = "ooll"
print(re.search(r"o+l+","oil")) # match = None because i comes in between them


# The repeating_letter_a function checks if the text passed includes the letter "a"
#  (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True,
#  while repeating_letter_a("pineapple") is False. Fill in the code to make this work.
import re
def repeating_letter_a(text):
  result = re.search(r"a+.*a+",text,re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

#soln 2
import re
def repeating_letter_a(text):
  result = re.search(r"A|a]+.*[A|a]+",text,re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

 


import requests.api
import re
# ? = 0/1 occurence of a char
print(re.search(r"p?each","To each their own")) # each
print(re.search(r"p?each","I like Peaches")) #peach

#escaping characters
print(re.search(r".com", "welcome")) # lcom , not true
print(re.search(r"\.com", "welcome")) # none , true
print(re.search(r"\.com","owen@google.com")) #.com

# \w = matches any alphanumeric charater, numbers ,values ,underscore
print(re.search(r,"\w*","This is a new example")) # 0-4
print(re.search(r"\w*","This_is_a_new_example")) # 0-19

#\d-digits, \s-white spaces,tabs,newline    \b - word boundaries



#Code to check if the text passed has at least 2 groups of alphanumeric characters
#(including letters, numbers, and underscores) separated by one or more whitespace characters.

import re
def check_character_groups(text):
  result = re.search(r"\w\s\w*", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False




import re

# Regular expression in action with real simulation scenarios

#words that start and end with a (A.*a)

#Countries starting and ending with A
print(re.search(r"A.*a","Argentina")) # True, Argentina
print(re.search(r"A.*a","Azurenan")) # no complete "Azurea" cutting of the string
print(re.search(r"^A.*a$","Azureanan")) # incomplete now , "Azureanan"  = None
print(re.search(r"^A.*a$","Australia")) #complete

# check for valid variable names
pattern  = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern,"This_si_a_valid_user_name")) # true


# Fill in the code to check if the text passed looks like a standard sentence,
# meaning that it starts with an uppercase letter,
# followed by at least some lowercase letters or a space, and ends with a period,
# question mark, or exclamation point.

import re
def check_sentence(text):
  result = re.search(r"^[A-Z][ |a-z]*[.!\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


# practice quiz and solution, but practice first before you see the solution

# 1.0
# Question 1
# The check_web_address function checks if the text passed qualifies as a top-level
# web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores),
# as well as periods, dashes, and a plus sign, followed by a period and a character-only
# top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape
# characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and
# character classes.

import re
def check_web_address(text):
  pattern = r"^[a-zA-Z_\-\+]+\.[a-zA-Z_\-\+]+\.?[a-zA-Z_\-\+]+$" # or ^[\w\-\.\+]+(\.)[a-zA-Z]+$
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

# 2.0
# The contains_acronym function checks the text for the presence of 2 or more characters
# or digits surrounded by parentheses, with at least the first character in uppercase
#  (if it's a letter), returning True if the condition is met, or False otherwise. For
#    example, "Instant messaging (IM) is a set of communication technologies used for
#    text-based communication" should return   True since (IM) satisfies the match conditions." Fill in the regular expression in this function:

import re
def contains_acronym(text):
  pattern = ___ 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

#soln
import re
def contains_acronym(text):
  pattern =r"\([A-Z0-9][A-Za-z]*\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


# 3.0
# Fill in the code to check if the text passed includes a possible U.S. zip code,
# formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits.
#  The zip code needs to be preceded by at least one space, and cannot be at the start of the text.

import re
def check_zip_code (text):
  result = re.search(r"___", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

# soln
import re
def check_zip_code (text):
  result = re.search(r"\s[0-9]{5}(-[0-9]{4})?", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False



# 4.0
# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between
# 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional
# space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many
# of the concepts that you just learned can you use here?

import re
def check_time(text):
  pattern = _______
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


#soln
import re
def check_time(text):
  pattern = r"^[1-9][0-2]?:[0-5][0-9] ?[AM|PM|am|pm]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False



# Advanced Regular Expression
# ADVANCED REGULAR EXPRESSION 

# capturing Groups
# Portions of patterns enclosed in parenthesis
import re
#create a script for matching first and last name
result = re.search(r"^(\w*),(\w*)$","Timz,Owen")
print(result)
print(result.groups()) #prints groups
print(result[0]) # access first group element
print(result[1])
print(result[2])
#rearrange
print("{} {}".format(result[2], result[1])) #rearrange using a different format


# Use functions to validate user names

def validate_user_names(name):
      results = re.search(r"^(\w*),(\w*)$", name)
      if results is None:
            return name
      return "{} {}".format(results[2], results[1])
print(validate_user_names("Timz,Owen")) # Owen Timz
print(validate_user_names("Timz, Owen, Mr.")) # Timz, Owen, Mr
print(validate_user_names("Mr,Owen")) # Owen Mr

# Fix the regular expression used in the rearrange_name function so that it
# can match middle names, middle initials, as well as double surnames.
import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

# soln
import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

# Repetition qualifiers

import re

# Match 5 String char letter
print(re.search(r"[a-zA-Z]{5}", "Timz Owens Cheba High schoo")) # use find all to find all matches
print(re.findall(r"[a-zA-Z]{5}","Timz Owens Cheba High schoo"))
print(re.findall(r"\b[a-zA-Z]{5}\b","Timz Owens Cheba High school")) # complete sentences

# match between ranges
print(re.findall(r"\w{5,10}","Timz Owens Chebara High school and a proffessional Developer"))

# find with specificc range
print(re.search(r"s\w{,20}","mr proffessor the developer is a prfessionanlly good"))


# The long_words function returns all words that are at least 7 characters.
#  Fill in the regular expression to complete this function.
import re
def long_words(text):
  pattern = re.findall(r"\w*"{7,})
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

# Extracting PID using Regex
import re

log = "July 31 07:51:30 mycomputer bad process[123456]: ERROR performing package upgrade"
regex = r"\[(\d+)\]"
results = re.search((regex, log))
print(results[1]) # prints [123456]

print(re.search(regex, "now the process has changed with [321654] here")) # prints 321654

print(re.search(regex, "lets try this [now]")) # throws an error

# solution is to use PID
# lets create a function here

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    results = regex.search(regex,log_line)
    if results is None:
        return ""
    return results[1]
print(extract_pid(log))


# Add to the regular expression used in the extract_pid function,
# to return the uppercase message in parenthesis, after the process id.
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]___"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(___)

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


#soln 
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]\: ([A-Z]{5,})"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


# spliting and Replacing
import re

print(re.split(r"[.?!]","statement 1 here, and this one too! and wouw?")) # no symbols printed

print(re.split(r"([.?!])", "statement 1 here, and this one too! and wouw?")) # both statements and symbols

# sub
# email scenario
print(re.sub(r"[\w.%+-]+@[w.-]+", "[REDACTED]", "Receined email from my_net.2300@my_ex.com"))

#Replacing with sub
print(re.sub(r"^([\w.-]*), ([\w.-]*$)",r"\2\1","Timz, Owen")) # Owen Timz

