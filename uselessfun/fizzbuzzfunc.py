import time
choice = int(input("Input top number: "))

def topNumber(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print(str(num) + ' fizzbuzz')
        elif num % 3 == 0:
            print(str(num) + ' fizz')
        elif num % 5 == 0:
            print(str(num) + ' buzz')
        else:
            print(num)

print("Running the program...")
time.sleep(5)

topNumber(choice)