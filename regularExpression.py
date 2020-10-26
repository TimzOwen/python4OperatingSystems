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

 
