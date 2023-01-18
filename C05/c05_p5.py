#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.


import csv
with open('studentdetails.csv','r') as csv_f:
    csv_r =csv.DictReader(csv_f)
    for line in csv_r:
        print(line)
