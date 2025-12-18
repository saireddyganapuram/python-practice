class BankAccount:
    def __init__(self,balance):
        self.bal = balance
    def withdraw(self,amount):
        self.bal -= amount
        print("withdrawl is success")
    def deposit(self,amount):
        self.bal += amount
        print("deposit is success")
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
    def validate_deposit(self,amount):
        self.acc.deposit(amount)
    def check_balance(self):
        print("the current balance is :",self.acc.bal)

BA = BankAccount(5000)
A = ATM(BA)
A.validate_withdraw(3000)
A.validate_deposit(1000)
A.check_balance()
