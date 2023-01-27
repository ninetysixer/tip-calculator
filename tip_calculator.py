# ## Tip Calculator

# # Instructions

# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


# # Example Input

# ```
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# ```

# # Example Output

# ```
# Each person should pay: $19.93
# ```


# # Hint

# 1. [How to round a number to 2 decimal places in Python](https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal)
# 2. [How to limit a float to two decimal places in Python](https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python)




# Solution

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

per_person = (tip_percentage / 100 * total_bill + total_bill)/split
final_amount = round(per_person, 2)
final_amount = "{:.2f}".format(per_person) # to have 2 decimal points

print(f"Each person should pay: ${final_amount}")
