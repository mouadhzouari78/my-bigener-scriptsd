import random
def withdraw(amount , cash):
    cash -=int(amount)
    return cash
def money(amount , cash):
    cash +=int(amount)
    return cash

def pick():
    emojis = ("💰" , "🔔" , "🍋")
    randomizer = random.choice(emojis)
    return randomizer
def main():
    won = 0
    lost = 0
    deposited = 0
    withdrawed = 0
    print("****************************")
    print("WELCOME TO THE JACKPOT GAME")
    print("****************************")
    cash = input("how much money do you have:")
    while not cash.isdecimal():
        cash = input("how much money do you have (a number):")
    cash = int(cash)
    refrence = cash
    is_running = True
    while is_running:
                while is_running and cash < 50:
                      print("ur cash is low u cant gamble (minimum=50)")
                      question = input("do u wanna deposit more (y/n)")
                      if question == "y":
                           play_not = "3"
                           break
                      elif question == "n":
                          play_not = "5"
                          break
                      else:
                          print("give a valid answer")
                if cash >= 50:
                    print("1-gamble")
                    print("2-show balance")
                    print("3-deposit")
                    print("4-withdraw")
                    print("5-exit")
                    play_not = input("choose an option:")
                if play_not == "1":
                    print("***************************")
                    a = pick()
                    b = pick()
                    c = pick()
                    print(f"        |{a}|{b}|{c}|")
                    print("***************************")
                    if a == b and b == c:
                       print ("         YOU WON")
                       cash += 150
                       print("**********************************")
                       print(f"    you have {cash} now")
                       print("**********************************")
                       won += 150
                       lost -=150
                    else:
                       print("         YOU LOST")
                       cash -= 50
                       print("**********************************")
                       print(f"     u have {cash} left")
                       print("**********************************")
                       lost = lost - 50
                elif play_not == "2":
                    print("**********************************")
                    print(f"   ur current balance is {cash}")
                    print("**********************************")
                elif play_not == "5":
                    print("***************************")
                    print("   thank you for playing")
                    print("***************************")
                    resume = won+lost
                    if resume >= refrence:
                        print(f"    you won {won+lost}")
                    else:
                        print(f"   you lost {abs(won+lost)}")
                    is_running = False
                elif play_not == "4":
                    amount = (input("how much money do you want to withdraw"))
                    while not amount.isdecimal():
                        amount = input("type a valid amount")
                    cash = withdraw(int(amount), cash)
                    withdrawed = withdrawed - int(amount)
                    print("**********************************")
                    print(f"   you have {round(cash)} money left")
                    print("**********************************")
                elif play_not == "3":
                    amount = (input("how much money do u want to deposit"))
                    while not amount.isdecimal():
                        amount = input("type an amount :")
                    cash = money(int(amount), cash)
                    deposited = deposited + int(amount)
                    print("**********************************")
                    print(f"   u have{round(cash)} now")
                    print("**********************************")
                else:
                    print("***************************")
                    print("    give a valid answer")
                    print("***************************")



if __name__ == "__main__":
    main()
