import math
from typing import Union

class Calculator:
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y

    @staticmethod
    def subtract(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def divide(x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

    @staticmethod
    def logarithm(x: float) -> float:
        if x <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        return math.log10(x)

    @staticmethod
    def square(x: float) -> float:
        return x ** 2

    @staticmethod
    def square_root(x: float) -> float:
        if x < 0:
            raise ValueError("Square root is not defined for negative numbers")
        return math.sqrt(x)

    def calculate(self, operation: str, x: float, y: float = None) -> float:
        """
        Perform calculation based on the operation and provided numbers
        """
        operations = {
            '+': lambda: self.add(x, y),
            '-': lambda: self.subtract(x, y),
            '*': lambda: self.multiply(x, y),
            '/': lambda: self.divide(x, y),
            'log': lambda: self.logarithm(x),
            'square': lambda: self.square(x),
            'sqrt': lambda: self.square_root(x)
        }
        
        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")
            
        return operations[operation]() 