class staticMethod:
    def __init__(self,a):
        self.a = a
    @staticmethod
    def display(a):
        print(a)

sm = staticMethod(10)
sm.display(sm.a)
    
    