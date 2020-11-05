
# DATA STREAMS IN PYTHON

# Reading data  interactively
# user input

name = input("Enter your name")
print('Hello ' + name)

# different input  data types
def to_seconds(hours,minutes,seconds):
    return hours*3600 + minutes*60 + seconds
print('Welcome to our time convertion')
cont="y"
while(cont.lower() == "y"):
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    
    print("that's {} seconds".format(to_seconds(hours,minutes,seconds)))
    print()
    cont=input("Want to do another conversion? Press Y")
print("Welcome back Again")



# standard streams

#STDIN
#STDOUT
#STDERROR

# Environment variables
path variable
Echo
    echo $Path 
export missing Keys
    export FRUIT=pineapple

    
    
    
# CommandLine Arguments

# Exit status-->Commands provided to the shell 
check variable value(pass-0)
    wc variables.py
    echo $?
Errors(1)

# Atom create

import os
import sys

filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename,"w") as f:
        f.write("New file created\n")
else:
    print("Error, File {} exists".format(filename))
    sys.exit(1)
    


# summary 
# Taking an input from a user, raw_input should be used:
>>> my_number = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
1337
>>> print(my_number)
1337
>>>

# Now, this is important, because, raw_input does not evaluate an otherwise valid Python expression. In simple terms, 
# raw_input will just get a string from a user, where input will actually perform basic maths and the like. See below:
>>> my_raw_input = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1  # This is treated like a raw string.
>>> my_input = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1 # This is treated like an expression.
>>> print(my_raw_input)
123 + 1
>>> print(my_input)
124 # See that the expression was evaluated!



# python Subprocesses
import subprocess

>>>subprocess.run(["date"])
>>>(subprocess.run(["sleep",'2']))

#obtaining the output os a system Command
# check users logged ina comp wit WHO

results  = subprocess.run(["Host","8.8.8.8"], capture_output=true)
print(results.returncode)
print(results.stdout())
print(results.stdout.dencode.split())
# run a file not existing using the command and check the stdout error
results = subprocess.run(["rm","Does not exist"], capture_error=true) # 1 = fail
print(results.stdout)
print(results.stderr)


 ==================================================================================================Readme
# Python subprocesses

#changin path variable
import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

results = subprocess.run(["myapp"], env=my_env)


# Processing Log Files
# Filtering Log Files with Regular expression

import sys
logfile = sys.argv[1]
with open('logfile') as f:
    for line in f:
        if "CRON" not in line:
            continue
          # regex.
        import re

        pattern = r"USER \((\w+)\)$"
        liner = "Random user and server log message with the user name to be fecthed by the user"
        result = re.search(pattern, line)
        print(result[1]) # shpws the log file
        print(line.strip()) # create a regulax ti be used here





# We're using the same syslog, and we want to display the date, time, and process id that's 
# inside the square brackets. We can read each line of the syslog and pass the contents 
# to the show_time_of_pid function. Fill in the gaps 
# to extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.

#  soln
import re
def show_time_of_pid(line):
  pattern = pattern = r"^(\w{3}\s\d\s\d+:\d+:\d+).*\[(\d+)"  # or r"([\w :]{14}).*\[(\d+)" or #    pattern = r"(\w+ \d? \d+:\d+:\d+).*\[(\d{5})\]"
  result = re.search(pattern, line) 
  return "{} pid:{}".format(result[1], result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440



# UP NEXT ON GENERATORS


# Used to create iterators
# functions that return iterable items/elements one at a time
# uses yield instead of generators

def myCountGenerators():
    yield 10
    yield 20
    yield 30
    yield 40
my_g = myCountGenerators()
print(my_g) # <generator object myCountGenerators at 0x000001F3C66FBAC0>
#loop through to check the items
# for x in my_g:
#     print(x)

# get the items one by one
value_n = next(my_g)
print(value_n)

# calculate sum of yield
print(sum(my_g))

#print sorted gen
def myIntGenerators():
    yield 70
    yield 20
    yield 15
    yield 40
my_s_g = myIntGenerators()
print(sorted(my_s_g)) # sorts the elements


# count down while loops
def countingDown(startingNo):
    print('starting at {}', startingNo)
    while startingNo > 0:
        yield startingNo
        startingNo-=1
countDown = countingDown(5)
print(next(countDown))
print(next(countDown))
print(next(countDown))
print(next(countDown))
print(next(countDown))
# print(next(countDown))  # printing this throws a stop iteration ERROR

# working with large data
import sys

def appendingN(num):
    my_list = []
    start_n = 0
    while start_n<num:
        my_list.append(num)
        num +=1
    return my_list
print(appendingN(15))
print(sum(appendingN(10)))


# using generators instead of List to save on space
def appendWithGenerators(n):
    num = 0
    while num<n:
        yield num
        num +=1
print(sum(firstn(10)))
print(sum(appendingWithGenerators(10))

#check size
print(sys.getsizeof(appendingN((10)))
print(sys.getsizeof(appendWithGenerators(10)))



# GENERATORS SAMPLE 2
# using fobonacii series

def fibonacci(max_limit):
    # 0,1
    a,b = 0,1
    while a < max_limit:
        yield a
        a,b = b, a + b
fib  = fibonacci(30)
for i in fibonacci:
    print(i)



# Generator Expression:
# even numbers with for loop 
# simlified loopig of the commands in the for loop and saves on the spaces 
# almost similar to the list comprehension
myGenerator = (i for i in range(20) if i % 2 ==0)
for x in myGenerator:
    print(x)
   
# you can convert it to a list using the list
print(list(myGenerator))   
   
# list comprehension

myListComprehension = [x for x in range(10) if i % 3 == 0]
for i in myListComprehension:
    print(i)


# calculate the siz of a the list for the comparison





# THREADING VS MULTUPROCESSING
# running your code and making it fast

import sys

myListComprehension = [x for x in range(10) if i % 3 == 0]
for i in myListComprehension:
    print(sys.getsizeof(myListComprehension))

myGenerator = (i for i in range(20) if i % 2 ==0)
for x in myGenerator:
    print(sys.getsizeof(myCountGenerators))



# PROCESS


















