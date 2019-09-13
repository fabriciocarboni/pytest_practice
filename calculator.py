import numbers
import sys

class CalculatorError(Exception):
    """An exception class for Calculator"""


class Calculator:
    """A terrible Calculator"""

    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a + b


    def subtract(sefl, a, b):
        return a - b

    def multiply(sefl, a, b):
        return a * b

    def divide(sefl, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise CalculatorError("Can't divide by zero")
    
    def _check_operand(self, operand): #helper method _
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" was not a number')




if __name__ == "__main__":
    print("Let's calculate!")
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.multiply,
        calculator.divide
    ]
    while True:
        for i, operation in enumerate(operations, start=1): #builtin enumerate function
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        operation = input("Pick an operation: ")
        if  operation == 'q':
            sys.exit()
        op = int(operation)
        a = float(input("What is a? "))
        b = float(input("What is b? "))
        try:
            print(operations[op -1](a, b))
        except CalculatorError as ex:
            print(ex)
