print("Welcome to the Coffee machine")

num1 = "cappatino"
num2 = "latte"
num3 = "mocha"

def payment():
    pay = int(input("Please enter 3$\n"))
    if pay >= 3:
        ans = float(pay)-3
        print(ans)
        print("Here is your change")
    else:
        print("Please add more money")



def menu():
    menu = input("Please select options: \n"
                 "cappation / latte / mocha ")
    if menu == num1:
        print("Pay for your cappatino ")
    elif menu == num2:
        print("Pay for your latte")
    elif menu == num3:
        print("Pay for your mocha ")
    else:
        print("not working")


menu()
payment()


