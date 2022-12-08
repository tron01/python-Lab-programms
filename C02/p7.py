#Add ‘ing’ at the end of a given string. If it already 
# ends with ‘ing’, then add ‘ly’

def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1

s = input("Enter the string:")
print("Result:",add_string(s))


""" --------commented---- 

string.endswith(string)


"""