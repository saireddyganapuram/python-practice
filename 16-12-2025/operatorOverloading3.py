class operator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        x = self.a + other.a
        y = self.b + other.b
        return operator(x,y)
    def __mul__(self,other):
        x = self.a * other.a
        y = self.b * other.b
        return operator(x,y)
    def __sub__(self,other):
        x = self.a - other.a
        y = self.b - other.b
        return operator(x,y)
    def __truediv__(self,other):
        x = self.a / other.a
        y = self.b / other.b
        return operator(x,y)
    
ob1 = operator(10,20)
ob2 = operator(30,40)
ob3 = operator(50,60)
ob4 = operator(70,80)  
ob5 = operator(90,100)
ob6 = ob1 + ob2 * ob3 - ob4 / ob5
print(ob6.a , ob6.b)