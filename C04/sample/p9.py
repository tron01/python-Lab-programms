#Abstract class
from abc import ABC ,abstractmethod

class Aclass(ABC): #abstract class
    @abstractmethod #decorator
    def display(self):
        None
    @abstractmethod
    def show(self):
        None    
class Demo(Aclass): #concrete class
    def display(self):
        print("Abstract method")
    def show(self):
        print(" Abstract show ")
        
obj=Demo()
obj.display()
obj.show()

