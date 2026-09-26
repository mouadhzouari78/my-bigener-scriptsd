import random
start = input("do u wanna play (y/n)? : ")
if start == "y":
    guess =  ""
    guesses = 0
    number = random.randint(1,100)
    while guess != number:
        guesses += 1
        guess = int(input("guess the number : "))
        if guess > number:
            print("too high")
        elif guess < number:
            print("too low")
        else:
            print("you got it")
            print(f"it took {guesses} guesses")
else :
    print ("cancelled")
