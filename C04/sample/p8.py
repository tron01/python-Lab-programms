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
    # __ for private  
    def __display(self):
        print("Welcome!",self.__a)
    # __ show will access display! 
    def show(self):
        self.__display() 
obj = emp()
#print(obj.a)
obj.show()
