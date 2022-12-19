#mutliple inheri
class father:
    def display1(self):
        print("father class")
class mother:
    def display2(self):
        print(" mother class")

class child1 (father,mother):
    def show1(self):
        print("Child 1")

c1 = child1()

c1.display1()
c1.display2()
