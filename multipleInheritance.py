class c1:
    def m1(self):
        print("m1 from c1")
class c2:
    def m2(self):
        print("m2 from c2")
class c3:
    def m3(self):
        print("m3 from c3")
class c4(c1,c3,c2):
    def display(self):
        print("task done")

c = c4()
print(c4.mro())
c.m1()
c.m2()
c.m3()
c.display()