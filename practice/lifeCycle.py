class OLC:
    def __new__(cls):
        print("the object memory is created")
        return super().__new__(cls)
    def __init__(self):
        print("the object is intialized")
    def display(self):
        print("object is in use")
    def __del__(self):
        print("the object is deleted")
o = OLC()
o.display()
del o