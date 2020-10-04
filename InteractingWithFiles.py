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
