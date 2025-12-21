class student:
    def presentornot(self):
        print("student attended to class")
class training:
    def trainingmtd(self):
        print("training as IRTP")

class delegation:
    def __init__(self):
        self.s = student()
        self.t = training()
    def __getattr__(self, name):
        if(hasattr(self.s,name)):
            return getattr(self.s,name)
        elif(hasattr(self.t,name)):
            return getattr(self.t,name)
        else:
            print("give the corrext class")
d = delegation()
d.trainingmtd()
d.presentornot()