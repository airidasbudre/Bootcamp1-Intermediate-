from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    # if coffee_maker.is_resource_sufficient(drink=choice) == True:
    #     coffee_maker.make_coffee(order=choice)
    if choice == "report":
        coffee_maker.report()
    elif choice == "off":
        print("shut down")
        break
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


