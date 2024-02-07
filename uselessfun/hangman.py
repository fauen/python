import random
print("Welcome to the hangman game!")
word_list = ["apple", "banana", "orange", "lemon", "cherry"]
secret_word = random.choice(word_list)
guess = input("Guess a letter: ")

for letter in secret_word:
    if letter == guess:
        print("Correct!")
    else:
        print("Incorrect...")