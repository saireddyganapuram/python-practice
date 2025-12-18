class BankAccount:
    def __init__(self,balance):
        self.bal = balance
    def withdraw(self,amount):
        self.bal -= amount
        print("withdrawl is success")
class ATM:
    def __init__(self,acc):
        self.acc = acc
    def validate_withdraw(self,amount):
        if amount < 0:
            print("enter the valid amount")
        elif(self.acc.bal - amount < 1000):
            print("Insufficient balance")
        else:
            self.acc.withdraw(amount)

BA = BankAccount(5000)
A = ATM(BA)
A.validate_withdraw(3000)
A.validate_withdraw(6000)
A.validate_withdraw(-1000)
