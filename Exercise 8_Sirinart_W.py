username = input("Username : ")
password = input("Password : ")
if username == "gift" and password == "1234":
    print("Sucessfully log in !")
    print("----Welcome to FRUIT SHOP-----")
    print("What you would like to get for today ?")
    print("1. Banana     8 THB")
    print("2. Orange    10 THB")
    print("3. Apple     15 THB")
    userSelected = int(input("Item # "))
    if userSelected == 1:
        qtt = int(input("Quantity (pcs) : "))
        price = 8
        print("Total amount:", price * qtt, "THB")
    elif userSelected == 2:
        qtt = int(input("Quantity (pcs) : "))
        price = 10
        print("Total amount:", price * qtt, "THB")
    elif userSelected == 3:
        qtt = int(input("Quantity (pcs) : "))
        price = 15
        print("Total amount : ", price * qtt, "THB")
    print("Thank you & Have a great day")
else:
    print("Username/Password is incorrect !")
