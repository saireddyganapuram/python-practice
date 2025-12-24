class addcls:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        x = self.a + other.a
        y = self.b + other.b
        return addcls(x,y)
    
ob1 = addcls(10,20)
ob2 = addcls(30,40)
ob3 = addcls(50,60)
ob4 = ob1 + ob2 + ob3
print(ob4.a , ob4.b)