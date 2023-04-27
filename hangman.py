import random
from hangman_art import stages, logo
from hangman_words import word_list

# Defining the main function


def main():
    end_of_game = False
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6
    guesses = []
    display = []

    # appends '_' to display list
    for _ in chosen_word:
        display.append("_")

    # Prints the hangman logo
    print(logo)

    # Testing code
    print(f'Pssst, the solution is {chosen_word}.')

    # While the game has not ended and playerr lives are not exhausted continue asking for a letter
    while not end_of_game and lives > 0:
        # Ask the user for a letter
        guess = input("Guess a letter: ").lower()

        # If the guessed letter in the list of previous guesses
        if guess in guesses:
            print(f"You already guessed '{guess}'.")
            # Prints the word with blanks and already guessed correct letters
            print_display(display)
            # Prints the hangman ASCII art depending on the no. of lives left
            print_hangman(lives)
            continue

        # If the guessed letter not in the list of previous guesses
        else:
            # Append that guess to the existing list of guesses
            guesses.append(guess)
            # If guessed letter not in the word to be guessed
            if guess not in chosen_word:
                print(
                    f"You guessed '{guess}'. That's not in the word. You lose a life.")

                # Prints the word with blanks and already guessed correct letters
                print_display(display)

                # Subtract one life for guessing wrong
                lives -= 1

                if lives != 0:
                    # Prints the hangman ASCII art depending on the no. of lives left
                    print_hangman(lives)
            else:
                # If the guessed letter is in the word
                # Loop over ech character of the word and find the position of match
                for i in range(word_length):
                    if guess == chosen_word[i]:
                        # Update the 'display' list
                        display[i] = guess
                # Prints the word with blanks and already guessed correct letters
                print_display(display)
                # Prints the hangman ASCII art depending on the no. of lives left
                print_hangman(lives)

            # If no more blanks in the display
            # Player wins and game ends.
            if "_" not in display:
                end_of_game = True
                print("You won.")
                break

    # If all lives exhausted the its game over, player loses.
    if not end_of_game:
        print_hangman(lives)
        print("You lost.")

# A function that prints the word with blanks and already guessed correct letters


def print_display(blanks):
    for i in blanks:
        print(i, " ", end="")
    print("\n")

# A function thet prints the hangman ASCII art depending on the no. of lives left


def print_hangman(no_of_lives_left):
    print(stages[no_of_lives_left])


if __name__ == "__main__":
    main()
