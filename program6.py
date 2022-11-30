#Store a list of first names. Count the occurrences of ‘a’ within the list
names=["ashil","anand","ajeesh","aljo"]
count=0
for name in names:
    count=count+name.count('a')
    print("occurrences  of a in the list", name,"is:",count)
    count=0
