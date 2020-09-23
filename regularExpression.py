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
