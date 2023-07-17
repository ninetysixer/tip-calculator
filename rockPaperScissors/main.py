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

user_selection = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

if user_selection == "0":
  print(rock)
elif user_selection == "1":
  print(paper)
else:
  print(scissors)
  
computer_selection = random.randint(0, 2)

if user_selection == "0":
  if computer_selection == 0:
    print("\nComputer chose:\n" + rock + "\nIt's a draw, try again.")
  elif computer_selection == 1:
    print("\nComputer chose:\n" + paper + "\nYou lost.")
  elif computer_selection == 2:
    print("\nComputer chose:\n" + scissors + "\nYou win.")
elif user_selection == "1":
  if computer_selection == 0:
    print("\nComputer chose:\n" + rock + "\nYou win.")
  elif computer_selection == 1:
    print("\nComputer chose:\n" + paper + "\nIt's a draw, try again.")
  elif computer_selection == 2:
    print("\nComputer chose:\n" + scissors + "\nYou lost.")
elif user_selection == "2":
  if computer_selection == 0:
    print("\nComputer chose:\n" + rock + "\nYou lost.")
  elif computer_selection == 1:
    print("\nComputer chose:\n" + paper + "\nYou win.")
  elif computer_selection == 2:
    print("\nComputer chose:\n" + scissors + "\nIt's a draw, try again.")
