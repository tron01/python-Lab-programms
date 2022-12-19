#multi level inheri
class grandparent:
    
    def gp_show(self):
        print("grandparent class")

class parent(grandparent):
    num=123
    def display(self):
        print("parent class")

class child (parent):
    def show(self):
        print("Child class")
      
      
c = child()
c.display()
c.show()
c.gp_show()
print("Num is:",c.num)
