list_one: list[int] = []
list_two: list[int] = []
list_final: list[int] = []

def load_files():
    with open('list_one.txt', 'r') as file_one:
        for i in file_one:
            list_one.append(int(i))
    with open('list_two.txt', 'r') as file_two:
        for i in file_two:
            list_two.append(int(i))

def part_one():
    list_one_p1 = sorted(list_one)
    list_two_p1 = sorted(list_two)
    list_final_p1: int = 0

    for one, two in zip(list_one_p1, list_two_p1):
        list_final_p1 += abs(one - two)

    print(f"Part 1: {list_final_p1}")

def part_two():
    list_one_p2: list[int] = sorted(list_one)
    list_two_p2: list[int] = sorted(list_two)
    final_p2: int = 0
    
    for i in list_one_p2:
        final_p2 += i * list_two_p2.count(i)

    print(f"Part 2: {final_p2}")

def main():
    load_files()
    part_one()
    part_two()


if __name__ == "__main__":
    main()