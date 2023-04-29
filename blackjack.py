from art import logo
import os
from random import choice

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        clean()
        print(logo)
        player_cards = add_card(CARDS, 2)
        computer_cards = add_card(CARDS)

        computer_score = calculate_score(computer_cards)
        player_score = calculate_score(player_cards)

        print(
            f"    Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
        print(
            f"    Computer's first card: {computer_cards[0]}")

        while player_score < 21:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                player_cards.extend(add_card(CARDS))
                print(player_cards)
                player_score = calculate_score(player_cards)
                print(player_cards)
                print(
                    f"    Your cards: {player_cards}, current score: {player_score}")
                print(
                    f"    Computer's first card: {computer_cards[0]}")
            else:
                break

        while computer_score < 17:
            computer_cards.extend(add_card(CARDS))
            computer_score = calculate_score(computer_cards)

        print_final_result(player_cards, player_score,
                           computer_cards, computer_score)

        # if computer_score > 21:
        #     print(
        #         f"    Your final hand: {player_cards}, final score: {player_score}")
        #     print(
        #         f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

        #     print("Opponent went over. You win.")

        # elif player_score > 21:
        #     print(
        #         f"    Your final hand: {player_cards}, final score: {player_score}")
        #     print(
        #         f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

        #     print("You went over. You lose.")

        # elif computer_score < player_score:
        #     print(
        #         f"    Your final hand: {player_cards}, final score: {player_score}")
        #     print(
        #         f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

        #     print("You win.")

        # elif computer_score > player_score:
        #     print(
        #         f"    Your final hand: {player_cards}, final score: {player_score}")
        #     print(
        #         f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

        #     print("You lose.")

        # else:
        #     print(
        #         f"    Your final hand: {player_cards}, final score: {player_score}")
        #     print(
        #         f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

        #     print("It's a draw.")


def add_card(cards, n=1):
    added_cards = []
    for _ in range(n):
        added_cards.append(choice(cards))
    return added_cards


def calculate_score(scores):
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


def print_final_result(player_cards, player_score, computer_cards, computer_score):

    print(
        f"    Your final hand: {player_cards}, final score: {player_score}")
    print(
        f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    if player_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("Opponent went over. You win.")
    elif computer_score < player_score:
        print("You win.")
    elif computer_score > player_score:
        print("You lose.")
    else:
        print("Draw.")


def clean():
    """Function to clear a terminal"""
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


if __name__ == "__main__":
    main()
