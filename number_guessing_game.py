from random import randint

# Importing the logo from art.py
from art import LOGO

# Generating a random number between 1 and 100 (both included)
NUMBER = randint(1, 100)


def main():
    print(LOGO)
    print("Welcome to 'The Number Guessing Game'\nI'm thinking of a number beteen 1 and 100.")

    # print(f"The correct answer is {NUMBER}") #For debugging purpose

    # Asking the user for a difficulty level.
    # If a valid input is not given, the user is asked again and again and again ...
    while True:
        difficulty = input(
            "Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty not in ['easy', 'hard']:
            print("Enter a valid response.")
            continue
        else:
            break

    # Setting the number of attempts the user will have depending
    # on the difficulty level chosen by them
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    # The game logic
    # Asks the user to guess a number and checks if it's low or high or the correct guess
    # If guess not correct, ask again till the user runs out of attempts
    # At which point the user loses
    while True:
        # Asks for a guess using the 'make_guess' function
        guess = make_guess(attempts)

        # If the guess is not between 1 and 100, ask again; attempts not reduced
        if guess not in range(1, 101):
            print("The number should be between 1 and 100.")
            continue

        # Checks the number guessed against the correct number using the function 'check_guess'
        # The function itself prints the correct statement
        # The game ends if the user guesses the correct answer
        # If the user guesses wrong, the game continues
        if check_guess(guess, NUMBER):
            break
        else:
            pass

        # After every wrong answer, the number of attempts is reduced by 1
        attempts -= 1

        # If the user has no remaining attempts, the game end and the user loses
        # Else, the game continues and the user is asked again for a number
        if attempts != 0:
            print("Try to guess again.")
        else:
            print("You have run out of attempts.\nYou lose.")
            break


def make_guess(attempts: int) -> int:
    """Tells the user the number of attempts left and also asks the user 
    to guess a number. If an integer is not provided, prints an error message
    and asks the user again.

    Args:
        attempts (int): Number of attempts left

    Returns:
        int: An integer which is the number guessed by the user
    """
    print(f"You have {attempts} attempts remaining.")
    while True:
        try:
            guess = int(input("Guess a number: "))
            return guess
        except ValueError:
            print(
                "You did not enter a valid number.\nEnter a valid integer between 1 and 100 (both included).")
            continue


def check_guess(guess: int, answer: int) -> bool:
    """Checks the user's answer againt the correct answer and prints out the apppropriate statements 
    depending on whether the user's guess is too low, too high or just spot on. Also returns a boolean.

    Args:
        guess (int): The user's guess.

        answer (int): The correct answer.

    Returns:
        bool: Returns 'True' if the user guesses correctly, else returns 'False'.
    """
    if guess < answer:
        print("Your guess is too low.")
        return False

    elif guess > answer:
        print("Your guess is too high.")
        return False

    else:
        print(f"Yesss! You got it right. The number was {answer}")
        print("You win.")
        return True


if __name__ == "__main__":
    main()
