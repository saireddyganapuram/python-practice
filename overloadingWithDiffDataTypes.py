class overload:
    def add(self,*args):
        s = 0
        con = ""
        for x in args:
            if(x.isdigit()):
                s += int(x)
            else:
                con += x
        if(sum != 0):
            print("addition is :",s)
        if(con != ""):
            print("string concatination is :",con)

o = overload()
o.add("10","20","30")
o.add("hi"," hello"," good" ," morning")
o.add("10","hi","20"," hello","30", " good morning")
