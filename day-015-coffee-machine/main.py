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
    },
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order):
    coffee_ingredients = MENU[order]["ingredients"]
    for ingredient in coffee_ingredients:
        # Check if each resource in machine has enough for each coffee ingredient
        if resources[ingredient] < coffee_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(order):
    coffee_ingredients = MENU[order]["ingredients"]
    for ingredient in coffee_ingredients:
        resources[ingredient] -= coffee_ingredients[ingredient]


is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino):\n")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        if check_resources(order):
            cost = MENU[order]["cost"]
            money_inserted = process_coins()
            if money_inserted >= cost:
                change = round(money_inserted - cost, 2)
                print(f"Heres your change {change}")
                money += cost
                make_coffee(order)
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
