from menu import MENU, resources

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def make_coffee(coffee):
    if coffee == "espresso":
        coffee = MENU[coffee]
        name = "espresso"
        ingredients = coffee['ingredients']
        water = ingredients['water']
        coffee_bean = ingredients['coffee']
        resources['water'] -= water
        resources['coffee'] -= coffee_bean
        print(f"Here is your {name} ☕. Enjoy! ")
    elif coffee == "cappuccino":
        coffee = MENU[coffee]
        name = "cappuccino"
        ingredients = coffee['ingredients']
        water = ingredients['water']
        coffee_bean = ingredients['coffee']
        milk = ingredients['milk']
        if resources['water'] < water:
            return 0
        if resources['milk'] < milk:
            return 1
        if resources['coffee'] < coffee_bean:
            return 2
        resources['water'] -= water
        resources['coffee'] -= coffee_bean
        resources['milk'] -= milk
        print(f"Here is your {name} ☕. Enjoy! ")
    elif coffee == "latte":
        coffee = MENU[coffee]
        name = "latte"
        ingredients = coffee['ingredients']
        water = ingredients['water']
        coffee_bean = ingredients['coffee']
        milk = ingredients['milk']
        resources['water'] -= water
        resources['coffee'] -= coffee_bean
        resources['milk'] -= milk
        print(f"Here is your {name} ☕. Enjoy! ")


def check_resources(coffee):
    if coffee == "espresso":
        coffee = MENU[coffee]
        ingredients = coffee['ingredients']
        water = ingredients['water']
        coffee_bean = ingredients['coffee']
        if resources['water'] < water:
            return 0
        if resources['coffee'] < coffee_bean:
            return 2
    elif coffee == "latte":
        coffee = MENU[coffee]
        ingredients = coffee['ingredients']
        water = ingredients['water']
        coffee_bean = ingredients['coffee']
        milk = ingredients['milk']
        if resources['water'] < water:
            return 0
        if resources['milk'] < milk:
            return 1
        if resources['coffee'] < coffee_bean:
            return 2
    elif coffee == "cappuccino":
        coffee = MENU[coffee]
        ingredients = coffee['ingredients']
        water = ingredients['water']
        coffee_bean = ingredients['coffee']
        milk = ingredients['milk']
        if resources['water'] < water:
            return 0
        if resources['milk'] < milk:
            return 1
        if resources['coffee'] < coffee_bean:
            return 2


def report():
    remaining_water = resources['water']
    remaining_milk = resources['milk']
    remaining_coffee = resources['coffee']

    profit = resources['money']
    print(f"Water: {remaining_water}ml\nMilk: {remaining_milk}ml\nCoffee: {remaining_coffee}g\nMoney: ${profit}")


def coin_process():
    quarters = float(input('How many quarters? ($0.25): ')) * 0.25
    dimes = float(input('How many dimes? ($0.10): ')) * 0.10
    nickels = float(input('How many nickels? ($0.05): ')) * 0.05
    pennies = float(input('How many pennies? ($0.01): ')) * 0.01
    total_sum = quarters + dimes + nickels + pennies
    return total_sum


def check_transaction(coins):
    coffees_name = MENU['cappuccino']
    price_p = coffee_name['cost']
    if coins > price_p:
        change = coins - price_p
        resources['money'] += price_p
        print(f"Here is your change: ${change}")
        return True
    elif coins == price_p:
        resources['money'] += price_p
        return True
    else:
        return False


wants_to_drink = True
while wants_to_drink:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    while choice != "espresso" and choice != "latte" and choice != "cappuccino" and choice != "report" and choice != "off":
        choice = input("I am sorry I did not understand your selection, please enter again: ")
    if choice == "report":
        report()
    elif choice == "off":
        wants_to_drink = False
        print("Closing the machine. See you!")
    else:
        checking = check_resources(choice)
        if checking == 0:
            print("Sorry, there is not enough water.")
        elif checking == 1:
            print("Sorry, there is not enough milk.")
        elif checking == 2:
            print("Sorry, there is not enough coffee.")
        else:
            coffee_name = MENU[choice]
            price = coffee_name['cost']
            print(f"That would be ${price}. Please insert coins.")
            inserted_coins = coin_process()
            if check_transaction(inserted_coins):
                choice = make_coffee(choice)
            else:
                print("Sorry, that's not enough money. Money refunded.\n")
