class Divoverload:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __truediv__(self,other):
        self.x = self.a / other.a
        self.y = self.b / other.b
        return Divoverload(self.x,self.y)

A1 = Divoverload(30,40)
A2 = Divoverload(10,20)
A3 = A1 / A2
print(A3.a)
print(A3.b)