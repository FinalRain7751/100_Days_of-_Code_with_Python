from random import randint
from art import LOGO

NUMBER = randint(1, 101)


def main():
    print(LOGO)
    print("Welcome to 'The Number Guessing Game'\nI'm thinking of a number beteen 1 and 100.")
    print(f"The correct answer is {NUMBER}")
    while True:
        difficulty = input(
            "Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty not in ['easy', 'hard']:
            print("Enter a valid response.")
            continue
        else:
            break
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    while True:
        try:
            guess = make_guess(attempts)
        except ValueError:
            print(
                "You did not enter a valid number.\nEnter a valid integer between 1 and 100 (included).")
            continue

        if check_guess(guess):
            print("You win.")
            break
        else:
            pass
        attempts -= 1

        if attempts != 0:
            print("Try to guess again.")
        else:
            print("You have run out of attempts.\nYou lose.")
            break


def make_guess(attempts):
    print(f"You have {attempts} attempts remaining.")
    return int(input("Guess a number: "))


def check_guess(guess):
    number = NUMBER
    if guess < number:
        print("Your guess is too low.")
        return False

    elif guess > number:
        print("Your guess is too high.")
        return False

    else:
        print(f"Yesss! You got it right. The number was {number}")
        return True


if __name__ == "__main__":
    main()
