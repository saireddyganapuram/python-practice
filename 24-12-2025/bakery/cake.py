def cakes():
    print("CAKES MENU")
    print("1.black forest (price = $100)\n2.white forest (price = $150)\n3.straberry (price = $200)")
    choice = int(input("enter your choice : "))
    quatity = int(input("enter number of pieces : "))
    cakeBill = 0
    if(choice == 1):
        cakeBill += quatity * 100
    elif(choice == 2):
        cakeBill += quatity * 150
    elif(choice == 3):
        cakeBill += quatity * 200
    else:
        print("enter correct option")
    
    return cakeBill
