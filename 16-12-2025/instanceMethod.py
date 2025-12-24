class Demo:
    def __init__(self,a,b):
        print("The object is initialized")
        self.a = a
        self.b = b
    def add(self):
        print("The addition is :",self.a+self.b)
    def multiply(self):
        print("The multiplicaiton is :",self.a * self.b)

d = Demo(10,20)
d.add()
d.multiply()