from art import logo
import os
from random import choice

# List of cards' values avilable for the game
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        clean()
        print(logo)

        # Add 2 cards to the player's hand
        player_cards = add_card(CARDS, 2)
        # Adds 2 card to the Dealer's hand
        computer_cards = add_card(CARDS, 2)

        # Calculating the dealer's current score
        computer_score = computer_cards[0]
        # Calculating the player's current score
        player_score = calculate_score(player_cards)

        # Printing out the current status of the game
        print_current_status(
            player_cards, player_score, computer_cards)

        # Asking the player whether to 'hit' or 'stand'
        while player_score < 21:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                # Adds cards
                player_cards.extend(add_card(CARDS))

                # Calculates current score
                player_score = calculate_score(player_cards)

                # If player's score goes over 21 or if it is exactly 21
                # The game ends
                if player_score >= 21:
                    print_final_result(player_cards, player_score,
                                       computer_cards[:1], computer_score)
                    break

                # Printing the current status
                print_current_status(
                    player_cards, player_score, computer_cards)
            else:
                break

        # Revealing / adding cards to the Dealer's hand after the player stands
        # This block of code will not be executed if the player gets Blackjack or loses before the dealer's 2nd card is revealed
        computer_score = calculate_score(computer_cards)
        while computer_score < 17 and player_score < 21:
            computer_cards.extend(add_card(CARDS))
            computer_score = calculate_score(computer_cards)

            print_final_result(player_cards, player_score,
                               computer_cards, computer_score)

    # Clear screen and return to terminal
    clean()


def add_card(cards: list[int], n: int = 1) -> list[int]:
    """Adds 'n' number of cards to a player's/dealer's hand.

    Args:
        cards (list[int]): List of available cards' values.
        n (int, optional): Number of carsd to be added. Defaults to 1.

    Returns:
        list[int]: Returns a new list with the value of the newly added cards.

    """
    added_cards = []
    for _ in range(n):
        added_cards.append(choice(cards))
    return added_cards


def calculate_score(scores: list[int]) -> int:
    """A function to calculate scores in a game of Blackjack keeping in mind the rules (especially Aces).
    As an intentional side effect, it also alters the list and replaces '11' with '1' where necessary.

    Args:
        scores (list[int]): List containing the values of cards in a player's or dealer's hand

    Returns:
        int : Returns the total value of cards at that moment
    """
    total = 0

    for score in scores:
        total += score

    while total > 21 and 11 in scores:
        for i in range(len(scores)):
            if scores[i] == 11:
                total -= 10
                scores[i] = 1
                break
    return total


def print_current_status(player_cards: list[int], player_score: int, computer_cards: list[int]) -> None:
    """Prints the current status of the game.

    Args:
        player_cards (list[int]): List containing the values of the cards hels by the player
        player_score (int): Player's final score
        computer_cards (list[int]): List containing the values of the cards hels by the dealer
    """
    print(
        f"    Your cards: {player_cards}, current score: {player_score}")
    print(
        f"    Computer's first card: {computer_cards[0]}")


def print_final_result(player_cards: list[int], player_score: int, computer_cards: list[int], computer_score: int) -> None:
    """Checks the final scores in a game of Blackjack and prints the appropriate results.

    Args:
        player_cards (list[int]): List containing the values of the cards hels by the player
        player_score (int): Player's final score
        computer_cards (list[int]): List containing the values of the cards hels by the dealer
        computer_score (int): Dealer's final score

    Returns:
        Does not return anything. Just prints out the result.
    """
    print(
        f"    Your final hand: {player_cards}, final score: {player_score}")
    print(
        f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    if player_score > 21:
        print("You went over. You lose.\U0001F62D")
    elif player_score == 21:
        print("You got Blackjack. You win.\U0001F929")
    elif computer_score > 21:
        print("Opponent went over. You win.\U0001F601")
    elif computer_score == 21:
        print("Opponent got Blackjack. You lose.\U0001F62D")
    elif computer_score < player_score:
        print("You win.\U0001F601")
    elif computer_score > player_score:
        print("You lose.\U0001F62D")
    else:
        print("Draw.\U0001F641")


def clean() -> None:
    """Function to check the OS and clear the terminal with the appropriate command."""

    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


if __name__ == "__main__":
    main()
