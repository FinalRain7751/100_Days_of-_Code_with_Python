from helper import MENU, resources, clean


def main():
    # Declaring the global variable 'resources'
    global resources

    # Asking the user for the type of coffee he/she wants
    while True:
        user_input = input(
            "What would you like? (cappuccino/latte/espresso) ").strip().lower()
        if user_input not in ['cappuccino', 'latte', 'espresso', 'report', 'off']:
            continue
        break

    # If the user typed 'off', then quit the program
    if user_input == 'off':
        print("Coffee machine shutting down.")
        clean()
        return

    # If the user typed 'report', then print the current status of resources
    if user_input == 'report':
        print(
            f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} gm\nMoney: ${resources['money']}")
        main()

    # If the user wants coffee, then the following codes will be executed
    # First, check if the resources available is sufficient to make the cup of coffee
    # If resources insufficient, then apologize and print the name of item(s) missing
    return_of_is_sufficient = is_sufficient(user_input)
    if return_of_is_sufficient[0] == False:
        print_insufficient(return_of_is_sufficient[1:])

    # If sufficient resources available
    else:
        # Ask the user for money
        money = ask_for_money()

        # Cost of coffee stored in a variable
        cost = MENU[user_input]['cost']

        # If not enough money, refund money
        if money < cost:
            print("Sorry, that's not enough money. Money refunded.")

        # If money adequate, give coffee
        else:
            # If money more than the cost of coffee
            if money > cost:
                print(f"Here is ${round((money - cost), 2)} in change.")
            update_resources(user_input)
            print(f"Here is your {user_input}. Enjoy!")

    # Get ready for the next user
    main()


def is_sufficient(coffee_type: str) -> list:
    """Takes the name of a coffee type as input and returns a boolean and also a list of missing ingredients
    if needed.

    Args:
        coffee_type (str): The type of coffee the user wants

    Returns:
        list: First value: A boolean indicating if sufficient ingredients available or not.
              Subsequent values:  List of missing ingredients (only if sufficient ingredients not available).
    """
    return_list = []
    resources_needed = MENU[coffee_type]['ingredients']
    for key in resources_needed:
        if resources_needed[key] > resources[key]:
            if len(return_list) == 0:
                return_list.append(False)
                return_list.append(key.lower())
            else:
                return_list.append(key.lower())

    if len(return_list) == 0:
        return [True]
    return return_list


def print_insufficient(insufficient: list[str]) -> None:
    """Given a list of missing items prints a formatted string informing about the same.

    Args:
        insufficient (list[str]): List of missing items
    """
    finished = str()
    if len(insufficient) == 1:
        finished = insufficient[0]
    else:
        for i in range(len(insufficient)):
            if i == len(insufficient) - 2:
                separator = ' and'
            else:
                separator = ','
            finished += insufficient[i] + separator + " "
    print(f"Sorry, not enough {finished.strip().strip(',')}.")


def ask_for_money() -> float:
    """Asks for coins from a user and returns the total value of
       coins inserted in dollars

    Returns:
        float: Total value of coins inserted in dollars
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total_in_dollars = round((quarters * 0.25 + dimes * 0.10 +
                              nickles * 0.05 + pennies * 0.01), 2)

    return total_in_dollars


def update_resources(coffee_type: str) -> None:
    """Updates the global variable 'resources' depending on the ingredients needed to make that cup of coffee and it's
       cost.
    Args:
        coffee_type (str): The type of coffee the user ordered
    """
    global resources
    ingredients_needed = MENU[coffee_type]['ingredients']
    cost = MENU[coffee_type]['cost']

    for key in ingredients_needed:
        resources[key] -= ingredients_needed[key]

    resources['money'] += cost


if __name__ == "__main__":
    main()
