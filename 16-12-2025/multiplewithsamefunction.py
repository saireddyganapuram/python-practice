class c1:
    def m1(self):
        print("m1 from c1")
class c2:
    def m1(self):
        print("m2 from c2")
class c3:
    def m1(self):
        print("m3 from c3")
class c4(c2,c1,c3):
    def display(self):
        print("task done")

c = c4()
print(c4.mro())
c.m1()
c.display()