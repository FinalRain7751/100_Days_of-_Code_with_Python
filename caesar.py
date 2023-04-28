from helpers import ALPHABET, ART


def main():
    # Prints the ASCII art
    print(ART)
    # Defines a variable whose value will decide whether the loop will run or npt
    more = 'yes'
    while more == 'yes':
        # User input: encode or decode
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        # User input: Text to encode or decode
        text = input("Type your message:\n").lower()

        # User input: Number used to shift the letters
        shift = int(input("Type the shift number:\n"))

        # Encoding or decoding the text with relevant function
        if direction == "encode":
            message = encrypt(text, shift)
        else:
            message = decrypt(text, shift)

        # Printing out the encoded or decoded message
        print(f"Here's the {direction}d result: {message}")

        # User input: To continue or not
        more = input(
            "Type 'yes' if you want to go again. Otherwise type 'no' - \n")


# Function to encrypt a given text
def encrypt(text, shift):
    message = str()
    for i in range(len(text)):
        n = ALPHABET.index(text[i]) + shift
        if n > 26:
            n = n - 26
        message += ALPHABET[n]
    return message


# Function to decrypt a given text
def decrypt(text, shift):
    message = str()
    for i in range(len(text)):
        n = ALPHABET.index(text[i]) - shift
        if n < 0:
            n = 26 + n
        message += ALPHABET[n]
    return message


if __name__ == "__main__":
    main()
