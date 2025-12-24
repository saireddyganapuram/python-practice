class engine:
    def __init__(self,eng_name):
        self.eng_name = eng_name
    def display(self):
        print("the engine name is :",self.eng_name)
    def _pmethod(self):
        print("this is protected method")
class tyres:
    def __init__(self,ty_name):
        self.ty_name = ty_name
    def display(self):
        print("the tyres name is :",self.ty_name)
class body:
    def __init__(self,body_clr):
        self.body_clr = body_clr
    def display(self):
        print("the body color is :",self.body_clr)
class car:
    def __init__(self,name,eng_name,ty_name,body_clr):
        self.name = name
        self.eng_name = eng_name
        self.ty_name = ty_name
        self.body_clr = body_clr
    def result(self):
        print("the car name is :",self.name)
        ob1 = engine(self.eng_name)
        ob1.display()
        ob1._pmethod()
        ob2 = tyres(self.ty_name)
        ob2.display()
        ob3 = body(self.body_clr)
        ob3.display()
c = car("BMW","B58","pirelli","blue")
c.result() 
        