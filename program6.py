#Store a list of first names. Count the occurrences of ‘a’ within the list
names=["Ashil","Anand","Ajeesh","Aljo"]
count=0
for name in names:
    count=count+names.count('a')
    print("Occ of a in the list is:,"count)