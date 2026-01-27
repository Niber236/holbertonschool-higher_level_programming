# Python - Classes and Objects

This project creates a `Square` class and progressively adds functionality to understand Object-Oriented Programming (OOP) in Python.

## Technologies
* Python 3.8
* Ubuntu 20.04 LTS
* Style guidelines: pycodestyle (version 2.7)

## Files Description

| File | Description |
|Args|---------------------------------------------------------|
| `0-square.py` | Defines an empty class `Square`. |
| `1-square.py` | Defines a class `Square` with a private instance attribute `size`. |
| `2-square.py` | Adds validation for the `size` attribute (must be an integer >= 0). |
| `3-square.py` | Adds a public method `area()` that returns the current square area. |
| `4-square.py` | Adds getters and setters (`@property`) to access and update `size`. |
| `5-square.py` | Adds a public method `my_print()` that prints the square with the `#` character. |
| `6-square.py` | Adds a private instance attribute `position` with validation and updates printing. |

## Usage
Each file is an executable module. You can test the classes by importing them into a main file or running the provided test scripts.

Example for Task 1:
```python
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)