#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.


import csv

student =[{'No':1,'name':'joby','role':'student'},
          {'No':2,'name':'jack','role':'student'},
          {'No':3,'name':'john','role':'student'}]
csv_f =open('Name.csv','w')
field_name= list(student[0].keys())

csv_w  =csv.DictWriter(csv_f,fieldnames=field_name)
csv_w.writeheader()
csv_w.writerows(student)
csv_f.close()


csv_file=open('Name.csv','r')
csv_reader=csv.reader(csv_file)
#print (csv_reader)
for line in csv_file:
    print (line,end="")
