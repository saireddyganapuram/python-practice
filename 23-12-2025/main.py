from module1 import add as a1
from module1 import mul as m1
from module2 import add as a2
from module2 import mul as m2

x = int(input("Enter x value :"))
y = int(input("Enter y value :"))
z = int(input("Enter z value :"))

print(a1(x,y))
print(m1(x,y))
print(a2(x,y,z))
print(m2(x,y,z))