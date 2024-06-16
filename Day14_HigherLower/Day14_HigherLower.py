import Higher_Lower
import random

def random_index():
    return random.randint(0, len(Higher_Lower.data)-1)

a_index = random_index()
b_index = random_index()
score = 0

while True:
    print(f"\nCompare A: {Higher_Lower.data[a_index]['name']}, a {Higher_Lower.data[a_index]['description']}, from {Higher_Lower.data[a_index]['country']}")

    print(f"Against B: {Higher_Lower.data[b_index]['name']}, a {Higher_Lower.data[b_index]['description']}, from {Higher_Lower.data[b_index]['country']}")
    guess = input("\nWho has more followers? A or B?: ")
    
    if guess == 'A':
        if Higher_Lower.data[a_index]['follower_count'] > Higher_Lower.data[b_index]['follower_count']:
            score += 1
            print(f"\nYou're right! Current score: {score}")
            a_index = b_index
            b_index = random_index()
        else:
            print(f"\nSorry, that's incorrect. Final score: {score}")
            break
    elif guess == 'B':
        if Higher_Lower.data[b_index]['follower_count'] > Higher_Lower.data[a_index]['follower_count']:
            score += 1
            print(f"\nYou're right! Score: {score}")
            a_index = b_index
            b_index = random_index()
        else:
            print(f"\nSorry, that's incorrect. Final score: {score}")
            break
    else:
        print("\nInvalid! Please enter the correct input.")
        break