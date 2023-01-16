#Write a Python program to read each row from a given csv file and print a list of strings.
import pandas as pd


#csv_f = pd.read_csv("users.csv")
#print(csv_f)
print()
#print(csv_f.head())
"""
#specfic column
id=csv_f[["name","batch"]]
print(id)

"""
#print(csv_f.tail())
"""
csv_f = pd.read_csv("users.csv",usecols=["id","name"])
print(csv_f)
"""
import csv 

csv_f = open("users.csv")
csv_reader =csv.reader(csv_f)
for line in csv_f:
    print(line)
