#Sort dictionary in ascending and descending order. 
y={'carl':40,'alan':2,'bob':1,'danny':3} 
print(y)                                         
l=list(y.items())  
l.sort()           
print('Ascending order is: ',l) 
l=list(y.items())
l.sort(reverse=True) 
print('Descending order is: ',l)
