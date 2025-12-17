class student:
    def __init__(self,branch):
        self.branch = branch
    def display(self):
        print("the branch is :",self.branch)
class department:
    def __init__(self,sub,branch):
        self.sub = sub
        self.st = student(branch)
    def result(self):
        print("the sub is :",self.sub)
        self.st.display()
d = department("IRTP","IT")
d.result()