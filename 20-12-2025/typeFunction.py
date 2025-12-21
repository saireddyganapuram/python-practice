def user_info_init(self):
    print("__init__ is envoked")
def user_info_display(self):
    print("display function is envoked",self.x)

cls_name = "demo"
base = ()
dict1 = {
    "x" : 10,
    "__init__" : user_info_init,
    "display" : user_info_display
}

demo = type(cls_name,base,dict1)

d = demo()
d.display()
print(demo.mro())