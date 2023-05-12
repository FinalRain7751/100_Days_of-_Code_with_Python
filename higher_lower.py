# Importing the logos needed
from art import logo, vs
# Importing the data needed for the game
from game_data import data
from random import choice
import os

# Declaring a global variable for keeping scores
score = 0


def main():
    # Declaring the global variable 'score'
    global score

    # Clear the terminal
    clean()

    # Printing the game logo
    print(logo)

    # Printing winning statement if the user is correct
    if score > 0:
        print(f"You're right! Current score: {score}")

    # Getting two persons to compare from the game data
    person_A = choice(data)

    # If somehow persons A and B are same or if somehow they have the same number of followers,
    # we discard the person_B and get a new person_B
    while True:
        person_B = choice(data)
        if person_B == person_A or compare(person_A, person_B) == 'Equal':
            continue
        else:
            break

    # Printing the necessary statements
    print("Compare A: ", end="")
    print_person(person_A)
    print(vs)
    print("Against B: ", end="")
    print_person(person_B)

    # Ask the player for answer
    while True:
        answer = input(
            "Who has more followers? Type 'A' or 'B': ").strip().upper()
        if answer not in ['A', 'B']:
            print("Enter a valid option: 'A' or 'B'")
            continue
        else:
            break

    # Comparing the user's answer to the actual truth
    if answer == compare(person_A, person_B):
        score += 1
        main()
    else:
        clean()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")


def clean() -> None:
    """Function to check the OS and clear the terminal with the appropriate command."""

    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def print_person(person: dict) -> None:
    """ Prints a person's name, description and country from a dictionary

    Args:
        person (dict): A dictionary containing relevant info about a person
    """

    name = person['name']
    description = person['description']
    country = person['country']

    print(f"{name}, a {description}, from {country}.")


def compare(person_A: dict, person_B: dict) -> str:
    """ Compares two persons' instagram followers

    Args:
        person_A (dict): A dictionary containing relevant info about a person
        person_B (dict): A dictionary containing relevant info about a person

    Returns:
        str: Returns 'A' or 'B' depending on whose followers are more
    """

    if person_A['follower_count'] > person_B['follower_count']:
        return 'A'
    elif person_B['follower_count'] > person_A['follower_count']:
        return 'B'
    else:
        return 'Equal'


if __name__ == "__main__":
    main()
