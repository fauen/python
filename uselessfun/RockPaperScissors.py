import random

UserWins = 0
CompWins = 0

Options = ["rock", "paper", "scissors"]

Menu = """
Rock/Paper/Scissors

H - Help
W - Wins
Q - Quit
""" 
print(Menu)

while True:
    UserInput = input("\nInput: ").lower()
    if UserInput == "q":
        break

    if UserInput == "w":
        print(f"\nYour wins: {UserWins}.")
        print(f"Computer wins: {CompWins}.")
    elif UserInput == "h":
        print(f"Input Rock, Paper och Scissors to play. Use H, W or Q for other options.")

    if UserInput not in Options:
        continue

    RandomNumer = random.randint(0, 2)
    CompPick = Options[RandomNumer]
    print(f"Computer picked {CompPick}.")
    
    if UserInput == "rock" and CompPick == Options[2]:
        print("You won!")
        UserWins += 1
    elif UserInput == "paper" and CompPick == Options[0]:
        print("You won!")
        UserWins += 1
    elif UserInput == "scissors" and CompPick == Options[1]:
        print("You won!")
        UserWins += 1
    elif UserInput == CompPick:
        print("Draw!")
    else:
        print("Computer won.")
        CompWins += 1

print(f"Final score was {UserWins} - {CompWins}.")