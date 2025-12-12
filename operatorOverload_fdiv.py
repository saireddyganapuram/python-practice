class FloorDivoverload:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __floordiv__(self,other):
        self.x = self.a // other.a
        self.y = self.b // other.b
        return FloorDivoverload(self.x,self.y)

A1 = FloorDivoverload(30,40)
A2 = FloorDivoverload(10,20)
A3 = A1 // A2
print(A3.a)
print(A3.b)