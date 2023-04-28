from helpers import clean, logo


def main():
    print(logo)
    print("Welcome to the secret auction program. \n")
    bidders = []
    more_bidders = 'yes'
    while more_bidders == 'yes':
        add_bidders(bidders)
        more_bidders = input(
            "Are there any other bidders? Type 'yes' or 'no'.\n")
        clean()

    winning_bid = sorted(bidders, key=lambda b: b["bid"], reverse=True)[0]
    print(
        f"The winner is {winning_bid['name']} with a bid of ${winning_bid['bid']}")


def add_bidders(bidders):
    name = input("What is your name?: ")
    bid = int(input("What's ypur bid?: $"))
    bidders.append({
        "name": name,
        "bid": bid
    })


if __name__ == "__main__":
    main()
