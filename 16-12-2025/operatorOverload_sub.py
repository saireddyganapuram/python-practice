class Suboverload:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __sub__(self,other):
        self.x = self.a - other.a
        self.y = self.b - other.b
        return Suboverload(self.x,self.y)

A1 = Suboverload(30,40)
A2 = Suboverload(10,20)
A3 = A1 - A2
print(A3.a)
print(A3.b)