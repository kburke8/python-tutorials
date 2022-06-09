from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    else:
        print("I can't make that.")