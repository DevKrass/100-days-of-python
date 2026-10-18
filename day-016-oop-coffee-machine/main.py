from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu_obj = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

is_on = True
while is_on:
    options = menu_obj.get_items()
    drink_name = input(f"What would you like? ({options}): ")
    if drink_name == "off":
        is_on = False
    elif drink_name == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
        drink = menu_obj.find_drink(drink_name)
        if coffee_maker_obj.is_resource_sufficient(
            drink
        ) and money_machine_obj.make_payment(drink.cost):
            coffee_maker_obj.make_coffee(drink)
