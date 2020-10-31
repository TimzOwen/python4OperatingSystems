
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
