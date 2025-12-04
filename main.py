class constr():
    def __init__(self,a,b):
        print('constructor is envoked')
        self.A = a
        self.B = b
        print(self.A+self.B)
c = constr(10,20)
c1 = constr(10,40)