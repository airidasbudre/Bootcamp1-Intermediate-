

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
# --------------------------------------------------------------
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

NAME = None

def coins_processing():
    global total
    twenty = int(input("How many 20 cents? "))
    ten = int(input("How many 10 cents? "))
    five = int(input("How many 5 cents? "))
    one = int(input("How many 1 cent? "))
    total = twenty * 0.2 + ten * 0.1 + five * 0.05 + one * 0.01
    if total > cost_of_coffee:
        return True
    else: 
        return False



# -------------------------------------------------------------

def check_resourses():
    recourses_option = []
    recourses_option = name["ingredients"]
    
    if not coffee == "espresso":
        if recourses_option["milk"] > resources["milk"]:
            milk = resources["milk"]
            print(f"There is not enough milk. There is only {milk}")
            return False
    if recourses_option["water"] > resources["water"]:
        water = resources["water"]
        print(f"There is not enough milk. There is only {water}")
        return False
    elif recourses_option["coffee"] > resources["coffee"]:
        coffee2 = resources["coffee"]
        print(f"There is not enough milk. There is only {coffee2}")
        return False
    else:
        print("yes")
        return True


# ----------------------------------------------------------------

def check_transaction():
    cost_of_coffee = name["cost"]
    print(cost_of_coffee)
    if total == cost_of_coffee:
        print("enough")
    elif total > cost_of_coffee:
        change = total - cost_of_coffee
        print(f"Your change is {change}")
        return True
    else:
        print(f"Coffee cost {cost_of_coffee}. You put only {total}")
        return False


# -----------------------------------------------------------------




# 1. Prompt user by asking ???What would you like? (espresso/latte/cappuccino):???
# a. Check the user???s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

coffee = input("What would you like? (espresso/latte/cappuccino): ")

if coffee == "report":
   print(resources)
else:
    name = MENU[coffee]
    if check_resourses() == True:
        if coins_processing() ==  True: 
            if check_transaction() == True:
                print("make coffee")


cost_of_coffee = name["cost"]
cost_of_coffee2 = float(cost_of_coffee)

# 2. Turn off the Coffee Machine by entering ???off??? to the prompt.
# a. For maintainers of the coffee machine, they can use ???off??? as the secret word to turn off
# the machine. Your code should end execution when this happens.


# 3. Print report.
# a. When the user enters ???report??? to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: ???Sorry there is not enough water.???
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

    
   
if check_resourses() == True:
    if coins_processing() ==  True: 
       if check_transaction() == True:
          print("make coffee")
   




# {}
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say ???Sorry that's not enough money. Money refunded.???.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time ???report??? is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. ???Here is $2.45 dollars in change.??? The change should be rounded to 2 decimal
# places.


# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user ???Here is your latte. Enjoy!???. If
# latte was their choice of drink

