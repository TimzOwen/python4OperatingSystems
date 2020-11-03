# linux and windows test for py

# use latest python 
#use CML on windows and Terminal on linux

# print logs and len in google web site
import requests

response = requests.get("https://www.google.com")
len(response.text)

# DataFrames
import pandas

visitors = [123,456,789,987,654,312,159]
errors = [12,23,45,56,78,89,13]
df = pandas.DataFrame({"visitors":visitors,"errors":errors},index=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"])
print(df)
df["errors"].mean() #clean data to find mean.
print(df) #gives the mean
