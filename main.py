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

import random

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_input==0:
  print(rock)
  computer_input = random.randint(0,2)
  if computer_input==0:
    print("Computer chose Rock")
    print("It's a tie!")
  elif computer_input==1:
    print("Computer chose Paper")
    print("You lose!")
  elif computer_input==2:
    print("Computer chose Scissors")
    print("You win!")
elif user_input==1:
  print(paper)
  computer_input = random.randint(0,2)
  if computer_input==0:
    print("Computer chose Rock")
    print("You win!")
  elif computer_input==1:
    print("Computer chose Paper")
    print("It's a tie!")
  elif computer_input==2:
    print("Computer chose Scissors")
    print("You lose!")
elif user_input==2:
  print(rock)
  computer_input = random.randint(0,2)
  if computer_input==0:
    print("Computer chose Rock")
    print("It's a tie!")
  elif computer_input==1:
    print("Computer chose Paper")
    print("You win!")
  elif computer_input==2:
    print("Computer chose Scissors")
    print("It's a tie!")
else:  
  print("Invalid input")