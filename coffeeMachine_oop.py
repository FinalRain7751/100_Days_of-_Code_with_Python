from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def main():
    while True:
        order = (input(f"What would you like? ({menu.get_items()}) ")).lower()

        if order == "off":
            os.system("clear")
            return

        if order == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        menu_item = menu.find_drink(order)
        if not menu_item:
            continue

        if coffee_maker.is_resource_sufficient(menu_item):
            if not money_machine.make_payment(menu_item.cost):
                continue
            coffee_maker.make_coffee(menu_item)


if __name__ == "__main__":
    main()
