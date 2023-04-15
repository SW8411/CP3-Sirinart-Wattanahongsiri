username = input("Username : ")
password = input("Password : ")
if username == "admin" and password == "admin":
    print("------------------------------")
    print("   Welcome to Mellow Shop!!   ")
    print("------------------------------")
    print("1. Banana               THB 10")
    print("2. Orange               THB 15")
    print("3. Apple                THB 25")
    print("4. Papaya               THB 35")
    print("------------------------------")
    bananaPrice = 10
    orangePrice = 15
    applePrice = 25
    papayaPrice = 35
    userSelected1 = int(input("Your basket >> "))
    if userSelected1 == 1:
        qty = int(input("Quantity >> "))
        print("Total : THB ", bananaPrice*qty)
    elif userSelected1 == 2:
        qty = int(input("Quantity >> "))
        print("Total : THB ", orangePrice * qty)
    elif userSelected1 == 3:
        qty = int(input("Quantity >> "))
        print("Total : THB ", applePrice * qty)
    elif userSelected1 == 4:
        qty = int(input("Quantity >> "))
        print("Total : THB ", papayaPrice * qty)
    else:
        print("This is not available, please select again")
        userSelected2 = int(input("Your basket >> "))
        if userSelected2 == 1:
            qty = int(input("Quantity >> "))
            print("Total : THB ", bananaPrice * qty)
        elif userSelected2 == 2:
            qty = int(input("Quantity >> "))
            print("Total : THB ", orangePrice * qty)
        elif userSelected2 == 3:
            qty = int(input("Quantity >> "))
            print("Total : THB ", applePrice * qty)
        elif userSelected2 == 4:
            qty = int(input("Quantity >> "))
            print("Total : THB ", papayaPrice * qty)
    print("------------------------------")
    print("Thank you for shopping with us")
else:
    print("Your username/password is in correct. Please try again !")

