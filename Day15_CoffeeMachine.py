coffee_logo = """                                                                                       
                                      ██    ██    ██                                    
                                    ██      ██  ██                                      
                                    ██    ██    ██                                      
                                      ██  ██      ██                                    
                                      ██    ██    ██                                    
                                                                                        
                                  ████████████████████                                  
                                  ██                ██████                              
                                  ██                ██  ██                              
                                  ██                ██  ██                              
                                  ██                ██████                              
                                    ██            ██                                    
                                ████████████████████████                                
                                ██                    ██                                
                                  ████████████████████                                                                                                                        
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "milk": 50,#200,
    "coffee": 100,
    "money": 0,
}

coins = {
    'Quarters': 0.25,
    'Dimes': 0.10,
    'Nickels': 0.05,
    'Pennies': 0.01,
}

def report(water=0, milk=0, coffee=0, money=0):
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    resources['money'] += money

def check_ingredients(coffee):
    if MENU[coffee]['ingredients']['water'] > resources["water"]:
        print("\nSorry, the machine is low on water.")
        return False
    elif MENU[coffee]['ingredients']['milk'] > resources["milk"]:
        print("\nSorry, the machine is low on milk.")
        return False
    elif MENU[coffee]['ingredients']['coffee'] > resources["coffee"]:
        print("\nSorry, the machine is low on coffee.")
        return False
    else:
        return True

def press_coins(quarters, dimes, nickels, pennies, coffee):
    i=0
    sum = 0
    received = [quarters, dimes, nickels, pennies]
    for key in coins:
        sum += coins[key] * received[i]
        i += 1
    if sum < MENU[coffee]['cost']:
        print("\nSorry, that's not enough money. Money refunded.")
    else:
        report(MENU[coffee]['ingredients']['water'], MENU[coffee]['ingredients']['milk'], MENU[coffee]['ingredients']['coffee'], MENU[coffee]['cost'])
        change = round(sum - MENU[coffee]['cost'], 2)
        print(f"\nHere is ${change} in change.")
        print(f"Here is your {coffee}! Enjoy!")

get_coffee = True
print("\nWelcome to the coffee machine!")
print(coffee_logo)

while get_coffee:
    coffee_action = input("\nWhat would you like?(Espresso/Latte/Cappuccino): ").lower()
    
    if coffee_action == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        
    elif coffee_action == 'espresso' or coffee_action == 'latte' or coffee_action == 'cappuccino':
        available = check_ingredients(coffee_action)
        if not available:
            continue
        else:
            print("\nPlease insert coins: ")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            press_coins(quarters, dimes, nickels, pennies, coffee_action)
    
    else:
        get_coffee = False
            