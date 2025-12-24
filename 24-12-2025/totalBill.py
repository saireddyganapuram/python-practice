from bakery import *

print("MENU")
print("1.cakes\n2.cooldrink\n3.food.py")
choice = int(input("enter your choice : "))
while(True):
    if(choice == 1):
        cakeBill = cakes()
        print(cakeBill)
    elif(choice == 2):
        cooldrinkBill = cooldrinks()
        print(cooldrinkBill)
