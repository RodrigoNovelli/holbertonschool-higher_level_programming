#!/usr/bin/python3
class Calculator:
    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def create_default(cls):
        """Class method to create a default instance of Calculator."""
        return cls()

# Demonstration of the static method
result = Calculator.add(5, 3)
print(f"The sum of 5 and 3 is: {result}")  # Output: The sum of 5 and 3 is: 8

# Demonstration of the class method
default_calculator = Calculator.create_default()
print(f"Default calculator instance created: {default_calculator}")  # Output: Default calculator instance created: <__main__.Calculator object at ...>