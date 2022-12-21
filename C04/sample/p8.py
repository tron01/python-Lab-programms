#Data Encapsulation



"""
class emp:
    a=10
    def display(self):
        print("Welcome!")
obj = emp()
print(obj.a)
obj.display()
"""
# __a for private
class emp:
    __a=10
    def display(self):
        print("Welcome!",self.__a)
       
obj = emp()
#print(obj.a)
obj.display()
