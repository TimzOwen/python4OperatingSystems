
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

















