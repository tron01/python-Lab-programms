#Add ‘ing’ at the end of a given string. If it already 
# ends with ‘ing’, then add ‘ly’

st=input("enter the string")
if st.endswith ("ing"):
    st+='ly'
elif len(st)>=3:
    st+='ing'
print(st)

""" 
string.endswith(string)
"""