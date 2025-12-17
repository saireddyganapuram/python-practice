class demo:
    @staticmethod
    def display():
        print("this is the display method")
class demo1(demo):
    @staticmethod
    def result():
        print("this is the result method")

d = demo1()
d.display()
d.result()
demo1.display()
demo1.result()