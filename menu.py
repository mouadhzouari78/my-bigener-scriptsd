def main():
    print("____________menu__________")
    menu = {"pizza" : 2 ,
            "popcorn" : 1 ,
            "salmon" : 8 ,
            "crab" : 5 ,
            "chicken" : 4 ,
            "golden ramzy steak" : 80 }
    cart = []
    total = 0
    for key, value in menu.items():
        print(f"{key:10} : {value:.2f}")
    print("____________menu__________")
    while True:
        choice = (input("Enter your order: ")).lower()
        if choice == "q":
          break
        elif menu.get(choice) is not None:
            cart.append (choice)
        else :
            print ("not in menu")
    print("you ordered")
    for food in cart:
        soum = menu.get(food)
        print(f"/{food} = {soum}" , end="/")
    print()
    for food in cart:
        total = total + menu.get(food)
    print (f"your total is: {total:.2f}")
if __name__ == "__main__":
    main()