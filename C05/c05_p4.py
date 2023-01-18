#Write a new csv file.

"""
import csv
csv_f =open('studentdetails.csv','r')

csv_r =csv.reader(csv_f)
print(csv_r)
"""

import csv
with open('studentdetails.csv','r') as csv_f:
    csv_r =csv.reader(csv_f)
    with open('newstudentdetails.csv','w') as csv_f2:
        csv_w =csv.writer(csv_f2)
        for line in csv_r:
            csv_w.writerow(line)
