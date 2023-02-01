import random

logo = """  _   _                 _                  _____                     _             
 | \ | |               | |                / ____|                   (_)            
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |
                                                                              __/ |
                                                                             |___/ """


print(logo)
print("Welcome to the Number Guessing Game!")
def play_game():
  number = random.randint(1,100)
  #print(f"Psst, the number you are looking for is {number}.")
  if difficulty == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
    while attempts != 0 and attempts != 99:
      users_guess = int(input("Make a guess: "))
      if users_guess == number:
        print("Congratulations, you found the number!")
        attempts = 99
      elif users_guess > number:
        print("\nLOWER.")
        attempts -= 1
      elif users_guess < number:
        print("\nHIGHER")
        attempts -= 1
      if attempts != 0 and attempts != 99:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining.")
      if attempts == 0:
        print(f"Sorry, you ran out of attempts. The number you were looking for was {number}")
  if difficulty == "hard":
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")
    while attempts != 0 and attempts != 99:
      users_guess = int(input("Make a guess: "))
      if users_guess == number:
        print("Congratulations, you found the number!")
        attempts = 99
      elif users_guess > number:
        print("\nLOWER.")
        attempts -= 1
      elif users_guess < number:
        print("\nHIGHER.")
        attempts -= 1
      if attempts != 0 and attempts != 99:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining.")
      if attempts == 0:
        print(f"Sorry, you ran out of attempts. The number you were looking for was {number}")
      
difficulty = input("  I am thinking of a number between 1 and 100. \n    Choose a difficulty. Type 'easy' or 'hard': ").lower()
start_game = True
while start_game:
  if difficulty == "easy" or difficulty == "hard":
    play_game()
    start_game = False
  else:
    print("I am sorry but you did not type 'easy' or 'hard'. Please try again. ")
    difficulty = input("Choose 'easy' or 'hard': ").lower()
