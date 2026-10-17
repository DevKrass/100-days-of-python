import art


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def calculate(num1, num2, chosen_op, operators_dict):
    operation = operators_dict[chosen_op]
    return operation(num1, num2)


operators = {"+": add, "-": sub, "*": mult, "/": div}


def calculator():
    print(art.logo)
    first_num = float(input("Type the first number:\n"))
    continue_calculation = True
    while continue_calculation:
        operator = input("Type a mathematical operator ('+', '-', '*', '/'):\n")
        second_num = float(input("Type the second number:\n"))

        result = calculate(first_num, second_num, operator, operators)

        print(f"{first_num} {operator} {second_num} = {result}")

        should_continue = input(
            f"Do you want to continue working with {result}. Type 'y' or 'n'.\n"
        )
        if should_continue == "y":
            first_num = result
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()


calculator()
