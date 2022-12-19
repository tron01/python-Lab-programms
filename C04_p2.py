#inheri
class parent:
    num=123
    def display(self):
        print("parent class")

class child (parent):
    def show(self):
        print("Child class")
      
      
c = child()
c.display()
c.show()
print("Num is:",c.num)
