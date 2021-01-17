import numbers
import sys

class CalculatorError(Exception):
    """An exception class for Calculator
    """

class Calculator():
    """A terrible calculator.
    """
    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        try:
            return a + b
        except TypeError:
            raise CalculatorError("You just triggered a TypeError!")
        except ValueError:
            raise CalculatorError("You just triggered a ValueError!")

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a // b
        except ZeroDivisionError:
            raise CalculatorError("Can't divide by zero!")

    def _check_operand(self, operand):
        """Should only accept numbers as input.
        """
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" was not a number')


if __name__ == "__main__":
    # A small command-line helper
    print("Let's calculate!")
    calculator = Calculator()
    operations = [calculator.add, 
    calculator.subtract, 
    calculator.multiply, 
    calculator.divide]
    while True:
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        operation = input("Pick an operation:")
        if operation == "q":
            sys.exit()
        else:
            print(f"{operation} selected.")
        op = int(operation)

        # Assume the happy case, 
        # where the user inputs something which the float() function accepts
        a = float(input("What is a? "))
        b = float(input("What is b? "))
        try:
            print(operations[op - 1](a, b))
        except CalculatorError as ex:
            print(ex)