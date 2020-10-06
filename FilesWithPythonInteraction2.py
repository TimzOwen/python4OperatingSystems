
#GENERATING CSV FILES
#create a list of the data to be saved and stored
hosts = [["workstation.local","192.168.25.46"],["websever.cloud", "10.2.5.6"]]
with open(hosts.csv ,"w") as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)
    
 
#READING AND WRITING FILES WITH DICTIONARIES
#case of dicReader
with open('software.csv') as software:
    reader = csv.dicReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"],row["users"]))
        

#case 2
#create a list
users = [{"name": "sol mansi", .......}] 
keys = ["name", "username","department"]
with open('by_department.csv','w') as by_department:
    writer = csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users) #prints data to teh formar./use ....cat by_department.csv 
  

#RECAP QUIZ PRACTICE
#We're working with a list of flowers and some information about each one. The create_file function writes this
#information to a CSV file. The contents_of_file function reads this file into records and returns the information in
# a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV 
#file into a dictionary using DictReader.

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  ___
    # Read the rows of the file into a dictionary
    ___
    # Process each item of the dictionary
    for ___:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))



#SOLN 
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    f = csv.DictReader(file)
    # Process each item of the dictionary
    for row in f:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

#Output 
a pink carnation is annual
a yellow daffodil is perennial
a blue iris is perennial
a red poinsettia is perennial
a yellow sunflower is annual





#Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning 
#it into a dictionary. How do you skip over the header record with the field names?
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  ___
    # Read the rows of the file
    rows = ___
    # Process each row
    for row in rows:
      ___ = row
      # Format the return string for data rows only

          return_string += "a {} {} is {}\n".format(___)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


#SOLN 
  import os
  import csv

  # Create a file with data in it
  def create_file(filename):
    with open(filename, "w") as file:
      file.write("name,color,type\n")
      file.write("carnation,pink,annual\n")
      file.write("daffodil,yellow,perennial\n")
      file.write("iris,blue,perennial\n")
      file.write("poinsettia,red,perennial\n")
      file.write("sunflower,yellow,annual\n")

  # Read the file contents and format the information about each row
  def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file 
    create_file(filename)

    # Open the file
    with open(filename) as f:
      # Read the rows of the file
      rows = csv.reader(f)
      headers = next(rows)
      # Process each row
      for row in rows:
        name, color, ty = row
        # Format the return string for data rows only

        return_string += "a {} {} is {}\n".format(name, color, ty)
    return return_string

  #Call the function
  print(contents_of_file("flowers.csv"))

#output
a carnation pink is annual
a daffodil yellow is perennial
a daffodil yellow is perennial
a iris blue is perennial
a poinsettia red is perennial
a sunflower yellow is annual






#HANDLING FILES
#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect ='empDialect')

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list
employee_list = read_employees('/home/student-04-1e77fee3e475/data/employees.csv')

print(employee_list)

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
        print(department_list)

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data
dictionary = process_data(employee_list)
    print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

write_report(dictionary, '/home/student-04-1e77fee3e475/data/report.txt')



#HANDLING FILES 
#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect ='empDialect')

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list
employee_list = read_employees('/home/student-04-1e77fee3e475/data/employees.csv')

print(employee_list)

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
        print(department_list)

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data
dictionary = process_data(employee_list)
    print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

write_report(dictionary, '/home/student-04-1e77fee3e475/data/report.txt')
