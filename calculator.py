# Data Types:
# integers => int() e.g., 1, 2
# floats => float() e.g., 1.4654, 2.5667
# boolean => bool() e.g., true, false
# string => str () e.g., "Hello"
choice = True

while choice:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    operator = input("Enter operator (+, -, /, *) ")
    if operator == "+":
        print(f"{number1} + {number2} = {number1+number2}")
        decision = input("Do you want to keep doing calculations? (Y/N)").upper()
        if decision == "N":
            choice = False
    elif operator == "-":
        print(f"{number1} - {number2} = {number1-number2}")
        decision = input("Do you want to keep doing calculations? (Y/N)").upper()
        if decision == "N":
            choice = False
    elif operator == "/":
        print(f"{number1} / {number2} = {number1/number2}")
        decision = input("Do you want to keep doing calculations? (Y/N)").upper()
        if decision == "N":
            choice = False
    elif operator == "*":
        print(f"{number1} * {number2} = {number1*number2}")
        decision = input("Do you want to keep doing calculations? (Y/N)").upper()
        if decision == "N":
            choice = False
    else:
        print("Invalid Operator.")

# = this is something
# == is that this? is i == 3
# > greater than
# < Less than
# <= less than or equal to
# >= greater than or equal to

""""""
