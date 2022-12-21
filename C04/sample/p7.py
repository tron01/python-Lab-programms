#method overriding
class parent:
    def travel(self):
        print("cycle")

class child (parent):
    def travel(self):
        print("Bike")
      
      
c = child()
p= parent()
c.travel()
p.travel()
