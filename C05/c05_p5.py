#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.


import csv
with open('studentdetails.csv','r') as csv_f:
    csv_r =csv.DictReader(csv_f)
    with open('studentdetails_Dict.csv','w') as csv_f2:
        fieldName =["Roll No","Student Name","Grade","CO1","CO2","CO3","CO4","CO5"]
        csv_w =csv.DictWriter(csv_f2 ,fieldnames=fieldName)
        csv_w.writeheader()
        for line in csv_r:
            csv_w.writerow(line)     
