import random

TopNumber = input("Input a number: ")

# Here we check the the variable is a digit.
if TopNumber.isdigit():
    # We convert the variable here to an integer
    TopNumber = int(TopNumber)
    # Making sure the number is greater than 0
    if TopNumber <= 0:
        print("Something bigger than 0 please.")
        quit()
else:
    print("We need a number.")
    quit()

RandomNumber = random.randint(1, TopNumber)
Guesses = 0

while True:
    GuessesLeft = 3 - Guesses
    print(f"You have {GuessesLeft} guesses left.")
    Guesses += 1
    Guess = input("Guess the number: ")
    if Guess.isdigit():
        Guess = int(Guess)
    else:
        print("We need a number.")
        continue

    if Guess == RandomNumber:
        print(f"You guessed the correct number {RandomNumber}!")
        break
    elif GuessesLeft <= 1:
        print(f"\nYou have used your {Guesses} guesses. Better luck next time!")
        quit()
    elif Guesses > RandomNumber:
        print("You were above\n.")
    elif Guesses < RandomNumber:
        print("You were below\n")

print(f"You got it in {Guesses} guesses!")