password = input("Enter your password: ")
difficulty = 0
if(len(password) >= 8 and len(password) <= 16):
    difficulty += 1
for i in password:
    if(i.islower()):
        difficulty += 1
        break
for i in password:
    if(i.isupper()):
        difficulty += 1
        break
for i in password:
    if(i.isdigit()):
        difficulty += 1
        break
for i in password:
    if(not(i.islower() or i.isupper() or i.isdigit())):
        difficulty += 1
        break
if(difficulty == 5):
    print("the password is strong")
elif(difficulty >= 3):
    print("the password is good")
elif(difficulty >= 2):
    print("the password is poor")
else:
    print("the password is very poor")
