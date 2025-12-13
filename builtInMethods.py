class demo:
    def diplay(self):
        print("this is the display method")
class demo1(demo):
    def result(self):
        print("this is the result method")

o = demo1()
print(dir(demo1))
print(type(o))
print(isinstance(o,demo1))
print(issubclass(demo1,demo))

