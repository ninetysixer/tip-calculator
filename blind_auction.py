from replit import clear
from art import logo        #--------------------------------------------------------------------step 1: showing the logo from art.py

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

continue_auction = True
dictionary = {}

def bidding():   
  name = input("What is your name?: ")    #--------------------------------------------------step 2: asking for name input
  bid = input("What's your bid?: $")    #----------------------------------------------------step 3: asking for bid price
  dictionary[name] = bid      #------------------------------------------------------------- step 4: addding the inputs to the dictionary

while continue_auction:
  bidding()
  other_bidders = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
  if other_bidders == "yes":
    clear()
  elif other_bidders == "no":
    continue_auction = False
    max_value = max(dictionary, key=dictionary.get)
    max_bid = dictionary[max_value]
    print(f"The winner is {max_value} with a bid of ${max_bid}.")
  

  
