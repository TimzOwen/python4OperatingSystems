# Find and fix the error
#!/usr/bin/env python3
import numpy as np

def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = numpy.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y
print(numpyArray())

# soln 
#!/usr/bin/env python3
import numpy as np

def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = np.array([[3, 6, 2], [9, 12, 8]], np.int32) #make sure numpy var is correct
    return x*y
print(numpyArray())


#Check on Computer usage and free space availability
import shutil
du = shutil.disk_usage("/")
print(du) # usage(total=214605754368, used=203108868096, free=11496886272)



#Calculate CPU usage
import psutil
psutil.cpu_percentage(0.1)

#FUCNTION TO CHECK FOR CPU AND OS USAGE:

#!/user/bin/ env python3

import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free>20
def check_Cpu_usage():
    usage = psutil.cpu_percentage(1)
    return usage <75
if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!!!")
else:
    print("EVERYTHING OK")
