#Abstract class
from abc import ABC ,abstractmethod

class Aclass(ABC): #abstract class
    @abstractmethod #decorator
    def display(self):
        None
class Demo(Aclass): #concrete class
    def display(self):
        print("Abstract method")

obj=Demo()
obj.display()

