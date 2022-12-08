#Accept a list of words and return length of longest word

def longestLength(words):
    maxLenList = []
     
    for word in words:
        maxLenList.append((len(word), word))
     
    maxLenList.sort()
     
    print("The word with the longest length is:", maxLenList[-1][1],
          " and length is ", len(maxLenList[-1][1]))
 

a = ["one", "two", "third", "four"]
longestLength(a)