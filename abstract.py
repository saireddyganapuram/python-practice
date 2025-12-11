from abc import ABC,abstractmethod

class ABS(ABC):
    @abstractmethod
    def details(self):
        pass
    def display(self):
        print("this is display method")
class ABSInherit(ABS):
    def details(self):
        print("details is abstracted successfully")
class user2(ABS):
    def details(self):
        print("I took few examples")

A = ABSInherit()
A.details()
A.display()
u = user2()
u.details()
