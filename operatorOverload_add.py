class Addoverload:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        self.x = self.a + other.a
        self.y = self.b + other.b
        return Addoverload(self.x,self.y)

A1 = Addoverload(10,20)
A2 = Addoverload(30,40)
A3 = A1 + A2
print(A3.a)
print(A3.b)