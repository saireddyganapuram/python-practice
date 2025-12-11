class overload:
    def add(self,a,b,*args):
        s = a + b
        for x in args:
            s += x
        print("addition is ",s)

o = overload()
o.add(10,20,30)
o.add(10,20,30,40)
