from art import logo
import random
from replit import clear

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

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(userscore, computerscore):
  if userscore > 21 and computerscore > 21:
    return "You went over. You lose."

  
  if userscore == computerscore:
    return "It's a draw."
  elif computerscore == 0:
    return "Computer has Blackjack, Computer wins."
  elif userscore == 0:
    return "You have Blackjack, you win."
  elif userscore > 21:
    return "You went over, you lose."
  elif computerscore > 21:
    return "Computer went over, you win."
  elif userscore > computerscore:
    return "You win."
  else:
    return "You lose."
def play_the_game():
  
    print(logo)
  
    user_cards = []
    computer_cards = []
    should_continue = True
  
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    
    while should_continue:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f"    Your cards: {user_cards}, current score: {user_score}")
      print(f"    Computer's first card: {computer_cards[0]}")
    
      if computer_score == 0 or user_score == 0 or user_score > 21:
        should_continue = False
      else:
        user_decision = input("Type 'y' if you want to draw another card, type 'n' to pass: ")
        if user_decision == "y":
          user_cards.append(deal_card())
        else:
          should_continue = False
          
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
      should_continue = False

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
      
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_the_game()
  
