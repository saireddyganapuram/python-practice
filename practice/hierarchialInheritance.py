class Hierarchial:
    def details(self,a,b):
        self.a = a
        self.b = b
class sub1(Hierarchial):
    def add(self):
        print("addition is",self.a + self.b)
class sub2(Hierarchial):
    def mul(self):
        print("multiplication is",self.a * self.b)

s1 = sub1()
print(sub1.mro())
s1.details(10,20)
s1.add()

s2 = sub2()
print(sub2.mro())
s2.details(20,30)
s2.mul()