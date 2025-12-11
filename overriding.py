class overriding1:
    def display(self):
        print("this is the version 1")
class overriding2(overriding1):
    def display(self):
        print("this is the version 2")

o = overriding2()
o.display()