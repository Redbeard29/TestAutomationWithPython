def addition():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a + b)


def subtraction():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a - b)


def multiplication():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a * b)


def division():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a / b)

operation = input("Please type +, -, *, or /: ")

if operation == '+':
    addition()

elif operation == '-':
    subtraction()

elif operation == '*':
    multiplication()

elif operation == '/':
    division()

else:
    print("Operation not supported.")