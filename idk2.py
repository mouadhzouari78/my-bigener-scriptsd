# banking program
def zina():
    print("_______________________")
def deposit(balance):
    deposit = float(input("enter ur deposit: "))
    balance2 = deposit + balance
    return print(f"ur new balance is {balance2}")
def withdraw(balance):
    minus = float(input("enter the amount u want to withdraw: "))
    balance2 = balance - minus
    return print(f"ur new balance is {balance2}")
def main():
    zina()
    print("         bank")
    zina()
    balance = float(input("enter ur balance: "))
    print(f"your balance is {balance}")
    choice = None
    while choice != "deposit" and choice != "withdraw" :
        choice = input("do u want to deposit or withdraw? ")
        if choice == "deposit" :
            deposit(balance)
        elif choice == "withdraw" :
            withdraw(balance)
        else:
            print("enter a valid choice")
main()
