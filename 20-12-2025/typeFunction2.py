class A:
    def methodA(self):
        print("this is the A class method")
class B(A):
    def methodB(self):
        print("this is the B class method")

def user_info_init(self):
    print("__init__ is envoked")
def user_info_display(self):
    print("display function is envoked",self.x)

cls_name = "demo"
base = (B,)
dict1 = {
    "x" : 10,
    "__init__" : user_info_init,
    "display" : user_info_display
}

demo = type(cls_name,base,dict1)

d = demo()
d.display()
d.methodA()
d.methodB()
print(demo.mro())