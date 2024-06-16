#Black jack
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    return random.choice(cards)

def initialize_cards():
    my_cards = []
    computer_cards = []
    for i in range(0,2):
        my_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    return my_cards, computer_cards

def sum_cards(cards):
    sum = 0
    for card in cards:
        sum += card
    return sum

def hit():
    my_cards.append(deal_cards())
    sum_my_cards = sum_cards(my_cards)
    if sum_my_cards > 21:
        print(f"\nYour final hand: {my_cards}, Your final score: {sum_my_cards}")
        print(f"Compter's final hand: {computer_cards}, Computer's final score: {sum_cards(computer_cards)}")
        print("\nYou went over. You lose! 😭")

def hand():
    sum_computer_cards = sum_cards(computer_cards)
    #print(f"Sum of computer cards = {sum_computer_cards}")
    sum_my_cards = sum_cards(my_cards)
    #print(f"Sum of my cards = {sum_my_cards}")
    
    if sum_my_cards == 21 and sum_my_cards > sum_computer_cards:
        print(f"\nYour final hand: {my_cards}, Your final score: {sum_my_cards}")
        print(f"Compter's final hand: {computer_cards}, Computer's final score: {sum_cards(computer_cards)}")
        print("\nBlack Jack! You win! 😎")
    
    while sum_computer_cards < 17:
        computer_cards.append(deal_cards())
        
    if sum_my_cards > sum_computer_cards:
        print(f"\nYour final hand: {my_cards}, Your final score: {sum_my_cards}")
        print(f"Compter's final hand: {computer_cards}, Computer's final score: {sum_cards(computer_cards)}")
        print("\nYou Win! 😄")
    elif sum_my_cards == sum_computer_cards:
        print(f"\nYour final hand: {my_cards}, Your final score: {sum_my_cards}")
        print(f"Compter's final hand: {computer_cards}, Computer's final score: {sum_cards(computer_cards)}")
        print("\nDraw! 🤞")
    else:
        print(f"\nYour final hand: {my_cards}, Your final score: {sum_my_cards}")
        print(f"Compter's final hand: {computer_cards}, Computer's final score: {sum_cards(computer_cards)}")
        print("\nSorry, you lose. 😔")


blackjack = True

while blackjack == True:
    play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n'. ").lower()
    print(logo)
    if play == 'y':
        my_cards, computer_cards = initialize_cards()
        reorder = True
        while reorder:
            if sum_cards(my_cards) and sum_cards(computer_cards) < 21:
                reorder = False
            else:
                my_cards, computer_cards = initialize_cards()
                
        print(f"\nYour cards: {my_cards}, current score: {sum_cards(my_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        card_move = input("\nType 'y' to get another card or type 'n' to pass: ").lower()
        
        if card_move == 'y':
            hit()
        else:
            hand()
    
    else:
        blackjack = False