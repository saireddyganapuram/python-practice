class Base:
    def __new__(cls,a,b):
        print("this is the base class new method")
        return super().__new__(cls)
    def __init__(self,a,b):
        print("this the base class init method")
        self.a = a
        self.b = b
    def add(self):
        print("addition is ",self.a+self.b)

class Derived(Base):
    def __new__(cls,x,y):
        print("this is the derived class new method")
        return super().__new__(cls,x,y)
    def __init__(self,x,y):
        print("this is the derived class init method")
        super().__init__(x,y)
        self.x = x
        self.y = y
    def mul(self):
        print("multiplication is ", self.a * self.b)

d = Derived(10,20)
d.add()
d.mul()