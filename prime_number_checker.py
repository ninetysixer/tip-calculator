import math

def prime_checker(number):
    if number > 1:
        for i in range(2, number):      #through for loop basically diving the number from 2 to number itself to see if it has a factor
            if (n % i) == 0:
                print("It's not a prime number.")
                break
        else:
                print("It's a prime number.")
    else:
        print("It's not a prime number.")   # any number below 1 is not a prime number.

n = int(input("Check this number: "))
prime_checker(number=n)
