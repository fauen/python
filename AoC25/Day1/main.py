#full_list = list(range(1, 99))
#starting_number = 50
current_number = 50
zero_count = 0
minus = "L"
plus = "R"

sequence = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
        ]

def minus():
    

def wrap_around(current_number, min_val=1, max_val=99):
    return ((current_number - min_val) % (max_val - min_val + 1)) + min_val


for num in sequence:
    if minus in num:
        print(f"Minus: {num}")
        num = num.strip("L")
        num = int(num)
        current_number = current_number - num
        print(current_number)
        if current_number == 0:
            zero_count += 1
    elif plus in num:
        print(f"Plus: {num}")
        num = num.strip("R")
        num = int(num)
        current_number = current_number + num
        print(current_number)
        if current_number == 0:
            zero_count += 1

print(zero_count)
