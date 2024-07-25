class FormulaError(Exception):
    pass

def calculate_result(args):
    if len(args) != 3:
        raise FormulaError("Invalid input: Please provide a formula with two numbers and an operator separated by spaces.")

    try:
        num1 = float(args[0])
        num2 = float(args[2])
    except ValueError:
        raise FormulaError("Invalid input: Unable to convert numbers to float.")

    operator = args[1]
    if operator not in ('+', '-'):
        raise FormulaError("Invalid input: Operator must be '+' or '-'.")

    if operator == '+':
        result = num1 + num2
    else:
        result = num1 - num2

    return result

if __name__ == "__main__":
    try:
        user_input = input("Enter a formula (e.g., 1 + 1): ")
        args = user_input.split()

        result = calculate_result(args)
        print("Result:", result)

    except FormulaError as e:
        print("Error:", e)

