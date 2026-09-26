import random
options = ("rock", "paper", "scissors")
player_choice = None
while player_choice != "q" :
    player_choice = input("select rock paper or scissors: ")
    choice = random.choice(options)
    if player_choice in options:
        if player_choice == "rock" and choice == "paper":
            print ("you win")
        elif player_choice == "paper" and choice == "rock":
            print ("you win")
        elif player_choice == "scissors" and choice == "paper":
            print ("you win")
        elif player_choice == choice :
            print ("a tie")
        else:
            print(f"bot selected {choice} sooo")
            print("you loose")
    elif player_choice == "q":
        break
    else:
        print ("give a valid choice (rock, paper, or scissors)")
print("game ended")