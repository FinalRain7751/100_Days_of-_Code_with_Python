from helpers import clean, logo


def main():
    OPERATIONS = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    print(logo)
    calculator(OPERATIONS)


def calculator(operations, loops=0, result=0):
    if loops == 0:
        result = float(input("Enter first number: "))

    for key in operations:
        print(key)
    operation = input("Select an operation from above: ")

    num = float(input("Enter next number: "))
    result1 = operations[operation](result, num)
    print(f"{result} {operation} {num} = {result1}")
    cont = input(
        f"Type 'y' to continue calculating with {result1}, else type 'n' to exit: ")
    if cont == 'y':
        loops += 1
        calculator(operations, loops, result1)
    else:
        clean()
        calculator(operations)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


if __name__ == "__main__":
    main()
