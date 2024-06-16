import random

my_number = random.randint(1,100)

level = input("Welcome to the number guessing game!\nChoose a difficulty level. Type 'easy' or 'hard': ")

if level == 'easy':
    i=10
    while i >= 0:
        print(f"You have {i} attempts remaining to make the guess.")
        guess = int(input("Make a guess: "))
        if guess > my_number:
            print("Too high!")
            print('Guess again.')
        elif guess < my_number:
            print("Too low!")
            print("Guess again.")
        else:
            print(f"Thats right! The number is {my_number}.")
            break
        i -= 1
    if i == 0:
        print("\nYou're out of turns! The number was {my_number}.")
else:
    i=5
    while i >= 0:
        print(f"You have {i} attempts remaining to make the guess.")
        guess = int(input("Make a guess: "))
        if guess > my_number:
            print("Too high!")
            print('Guess again.')
        elif guess < my_number:
            print("Too low!")
            print("Guess again.")
        else:
            print(f"Thats right! The number is {my_number}.")
            break
        i -= 1
    if i == 0:
        print("\nYou're out of turns! The number was {my_number}.")