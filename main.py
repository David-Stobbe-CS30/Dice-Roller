import random


def roll2Dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    print(f"{dice1}, {dice2} (sum: {sum})")
    return sum

exit = False
while(not exit):
    print("DICE ROLL SIMULATOR MENU")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 times")
    print("3. Roll dice 'n' times")
    print("4. Roll dice until Snake Eyes")
    print("5. Exit")
    option = int(input("Select an option (1-5): "))


    if option == 1:
        roll2Dice()
    elif option == 2:
        for i in range(5):
            roll2Dice()
    elif option == 3:
        n = int(input("How many times?: "))
        for i in range(n):
            roll2Dice()
    elif option == 4:
        while(True):
            if roll2Dice() == 2:
                print("SNAKE EYES")
                break
    elif option == 5:
        exit = True
