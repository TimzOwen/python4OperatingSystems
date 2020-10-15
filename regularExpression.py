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
      

