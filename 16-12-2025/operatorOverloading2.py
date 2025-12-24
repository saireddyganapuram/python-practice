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
    
ob1 = operator(10,20)
ob2 = operator(30,40)
ob3 = operator(50,60)
ob4 = ob1 + ob2 * ob3
print(ob4.a , ob4.b)