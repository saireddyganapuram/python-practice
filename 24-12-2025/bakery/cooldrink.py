def cooldrinks():
    print("COOLDRINK MENU")
    print("1.100 ml (price = $10)\n2.200 ml (price = $15)\n3.300 ml (price = $20)")
    choice = int(input("enter your choice : "))
    quatity = int(input("enter number of pieces : "))
    cooldrinkBill = 0
    if(choice == 1):
        cooldrinkBill += quatity * 10
    elif(choice == 2):
        cooldrinkBill += quatity * 15
    elif(choice == 3):
        cooldrinkBill += quatity * 20
    else:
        print("enter correct option")
    
    return cooldrinkBill
