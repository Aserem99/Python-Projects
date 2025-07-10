import random

while True:
    choice = input("Would you like to roll the die? (Y/N): ").upper()

    if choice == 'Y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'N':
        print("Thanks for playing!")
        break
    else:
        print('Invalid choice')
