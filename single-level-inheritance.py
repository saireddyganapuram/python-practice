class Base:
    def display(self):
        print("This is the Base class method")
class Derived(Base):
    def result(self):
        print("This the derived class method")

d = Derived()
print("with respect to derived class")
d.display()
d.result()
b = Base()
print("with respect to the base class")
b.display()
# b.result()