import random

def game(userPick: str, score: int):
    randomPickList = ["H", "T"]
    randomPick = random.choice(randomPickList)
    if randomPick == userPick:
        score = score + 1
        print(f"You won! Your score is {score}\n")
        return score
    else:
        print("You loose!\n")
        score = 0
        return score

def main(score: int):
    userPick = input(f"[H]eads or [T]ails?\n").upper()
    if userPick == "H" or userPick == "T":
        score = game(userPick, score)
        main(score)
    else:
        if userPick == "Q":
            quit()
        else:
            print("Just type one character H or T.\n")
            main(0)

if __name__ == "__main__":
    main(0)