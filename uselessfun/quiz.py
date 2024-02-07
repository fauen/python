# To get a feel for variables and if-statements I'm trying out making a quiz.

print("Welcome to my quiz!")
Name = input("Input your name: ")

print(f"Hi {Name}! Let's have some fun together!")

"""
I could have written it like this as well:
print("Hi " + Name + "! Let's have some fun together!")
But I think the first option is easier to write.
"""

Ready = input("Are you ready? ")
if Ready.lower() != "yes":
    print("Please come back later when you are ready.")
    quit()

Score = 0
print("Let's go!\n")
Question = input("What is the auther of this quiz name? ")
if Question.lower() == "daniel":
    print("Correct!\n")
    Score += 1
else:
    print("Incorrect.\n")

Question = input("What is the author's nickname? ")
if Question.lower() == "fauen":
    print("Correct!\n")
    Score += 1
else:
    print("Incorrect.\n")

Question = input("What is his age? ")
if int(Question) == 35:
    print("Correct!\n")
    Score += 1
else:
    print("Incorrect.\n")

Question = input("Are you having fun? ")
if Question.lower() == "yes":
    print("Good, good...\n")
    Score += 1
else:
    print("Sorry to hear that :(.\n")

Calc = int((Score / 4) * 100)
Result = print(f"\n{Name} you scored {str(Score)}. Which is {Calc}%.\n")
if Calc >= 50:
    print(f"You got a really good score {Name}!\nHopefully you will come back and play again!")
else:
    print(f"Your score wasn't the best {Name}...\nI hope next time it'll go better!")