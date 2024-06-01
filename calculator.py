import math


class Calculator:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
            "**": self.power,
            "sqrt": self.root,
            "%": self.per,
            "!": self.fac,
            "sin": self.sin,
            "cos": self.cos,
            "tan": self.tan,
            "ctan": self.ctan
        }

    def add(self, number1, number2):
        return number1 + number2

    def subtract(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def divide(self, number1, number2):
        try:
            return number1 / number2
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")

    def power(self, number1, number2):
        return math.pow(number1, number2)

    def root(self, number):
        try:
            if number < 0:
                raise ValueError("Cannot take the square root of a negative number")
            return math.sqrt(number)
        except ValueError as exc:
            raise ValueError(f"Error in root operation: {exc}")

    def per(self, number):
        return f"{number / 100}%"

    def fac(self, number):
        try:
            if number < 0:
                raise ValueError("Cannot take the factorial of a negative number")
            return math.factorial(number)
        except ValueError as exc:
            raise ValueError(f"Error in factorial operation: {exc}")

    def sin(self, number):
        return math.sin(number)

    def cos(self, number):
        return math.cos(number)

    def tan(self, number):
        return math.tan(number)

    def ctan(self, number):
        try:
            if number == 0:
                raise ValueError("Cannot take the cotangent of zero")
            return 1 / math.tan(number)
        except ValueError as exc:
            raise ValueError(f"Error in cotangent operation: {exc}")
