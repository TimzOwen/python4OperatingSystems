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

