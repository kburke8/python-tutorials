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
    "profit": 0.0
}


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['profit']}")


def check_resources(selected_drink):
    for ingredient in MENU[selected_drink]["ingredients"]:
        if resources[ingredient] < MENU[selected_drink]["ingredients"][ingredient]:
            return ingredient
    return ""


def make_drink(selected_drink):
    for ingredient in MENU[selected_drink]["ingredients"]:
        resources[ingredient] -= MENU[selected_drink]["ingredients"][ingredient]


def check_transaction(selected_drink, inserted_money):
    if inserted_money >= MENU[selected_drink]["cost"]:
        make_drink(selected_drink)
        resources["profit"] += MENU[selected_drink]["cost"]
        if inserted_money > MENU[selected_drink]["cost"]:
            print(f"Here is ${round(inserted_money - MENU[selected_drink]['cost'], 2)} in change.")

        print(f"Here is your {selected_drink}. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


machine_on = True
while machine_on:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if drink_choice == "report":
        print_report()
    elif drink_choice == "latte" or drink_choice == "espresso" or drink_choice == "cappuccino":
        resource_result = check_resources(drink_choice)
        if len(resource_result) > 0:
            print(f"Sorry there is not enough {resource_result}.")
        else:
            money = insert_coins()
            check_transaction(drink_choice, money)
    elif drink_choice == "off":
        machine_on = False
    else:
        print("Sorry, I can't make that.")
