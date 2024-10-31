import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

n1 = float(input("What's the first number?: "))
should_continue = True

while should_continue:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))

    if operation in operations:
        output = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {output}")
        n1 = output
    else:
        print("Sorry, that's not a valid operation!")

    should_restart = input(f"Type 'y' to continue calculating with {n1}, or type 'n' to start a new calculation: ").lower()


    if should_restart == "n":
        should_continue = False


