import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rsp = [rock, paper, scissors]

human = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
print(rsp[human])

computer = random.randint(0,2)
print(f"Computer chose {computer}")
print(rsp[computer])

if human == computer:
    print("Draw")
elif human == 0 and computer == 1:
    print("You lose!")
elif human == 0 and computer == 2:
    print("You win!")
elif human == 1 and computer == 0:
    print("You win!")
elif human == 1 and computer == 2:
    print("You lose!")
elif human == 2 and computer == 0:
    print("You lose!")
elif human == 2 and computer == 1:
    print("You win!")
else:
    print("Invalid!")