print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You a walking down a dusty road in an obsecure misty forest and you stumble upon a fork in the road. Where do you want to go? Type 'left' or 'right'. \n")
direction = direction.lower()
if direction == "left":
    water = input("You come to a lake and you can make out the silhouette of an island amidst the fog. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
    water = water.lower()
    if water == "wait":
        door = input("Good choice. You arrive at the island unharmed. Beyond the thicket of the trees, there is a house with three doors. One red, one yellow and one blue. Which colour do you choose?\n")
        door = door.lower()
        if door == "red":
            print("You are engulfed by a raging fire. Game over.")
        elif door == "blue":
            print("Looks like you have walked into the dragons lair. The dragon has killed you. Game over.")
        elif door == "yellow":
            print("Congratulations! You have found the treasure chest! You win!")
        else:
            print("Game over.")
    else:
        print("Alas! Unbeknownst to you, the lake has always been infested with deadly pirahnahs. Looks like you're dinner. Game over.")
else:
    print("Game over!")