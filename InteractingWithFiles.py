text = 'Sample Text to Save\nNew line!'

# notifies Python that you are opening this file, with the intention to write
saveFile = open('exampleFile.txt','w')

# actually writes the information
saveFile.write(text)

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()


#Reading files and editing with linux nano 

#READING and WORKING WITH FILES IN PYTHON
import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything ok")
# to run this file and fix the Permission denied use:
sudo chmod +x health_checks.py #gives an error
#Let's debug the issuite(0)
#open file using nano editor
nano health_checks.py
#make the necessary changes (75< and not 75>)
#save the files(ctr-o, Enter, ctrl x)
#runn the program again
./health_checks.py
"Evrything OK!"
#!/usr/bin/env python3
import requests
import socket
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost=="127.0.0.1"
def check_connectivity():
    request = requests.get("http://www.google.com")
    response=request.status_code
    return response==200

#!/usr/bin/env python3
import requests
import socket
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost=="127.0.0.1"
def check_connectivity():
    request = requests.get("http://www.google.com")
    response=request.status_code
    return response==200#!/usr/bin/env python3
from network import *
import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")
    
    
# Reading files from a computer
file = open("spider.txt")

#read file contents
print(file.readline()) #prints each line separate and called again prints the next line

#read from current line to the end line
print(file.read())

#close the file
file.close()

#Automatically close files when done:
with open("spideer.txt") as file:
    print(file.readline()) #python automatically closes the files at the end of the code
    
#ITERATING THROUGHT FILES
#capitalize the words of a file by each line
with open("spider.txt") as file:
    for line in file:
        print(line.Upper())
 
#remove the empty and new line character
with open("spider.txt") as file:
    for lines in file:
        print(lines.strip().upper())
        
#read contents of a file in a list
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

#Writing Files in python
with open("spider.txt", "w") as a file:
    file.write("I have overwritten all your data ") #return the number of characters in the double quotes
    

#MANAGING FILES AND DIRECTORIES
# OS modules allows all it to run on all OS

#delete a file
import os 
os.remove("novel.txt")
os.remove("novel.txt") # Fails because the file is already removed

#rename a file
import os 
os.rename("beforename.txt","current_name.txt")

#check if files exits using so.path
os.path.exits("current_name.txt") #returns true if the file exists


#More Files information:
#get size of a file in bytes
os.path.getsize("spider.txt") #159
#get last time modified
os.path.getmtime("spider.txt") #prints time in unix timestamp
#modify the time to more Huma readable
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp) # (2020 1, 5, 8 , 2 ,896563)

# Some more functions of the os.path module include getsize() and isfile() which get information on the file 
# size and determine if a file exists, respectively. In the following code snippet, what do you think will print if the file does not exist?
import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")  # File error as there is no such file
    

#Check for absolute path of a file
os.path.abspath("spider.txt")
'\home\user\spider.txt'

#get current working directory
print(os.getcwd())

#create directory 
mkdir  #works on both linux and windows OS
os.mkdir("new_dirctory")
#change directory
os.chdir("new_dir)
#remove directory
os.rmdir("new_directory")

#combining to check list and sub directories of a file:
import os 
os.listdir("website")
['index.html,'images',''icons']

dir = "website"
for name in os.listdir(dir):
    fullname = os.join(dir,name)
    if os.path.usdir(fullname):
        print("{} is a directory" .format(fullname))
    else:
        print("{} is a file".format(fullname))

website/images is a directory
website/index.html is a file

