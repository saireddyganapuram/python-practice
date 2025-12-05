class supDemo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
class superworking(supDemo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
    def mul(self):
        print(self.x * self.y)

sw = superworking(10,20)
sw.add()
sw.mul()