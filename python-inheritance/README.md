# Python - Inheritance

This project focuses on the concept of Inheritance in Python programming. The goal is to understand how to create a class that derives attributes and methods from another class (superclass).

## General Concepts

* **Inheritance:** How to define a class that inherits from another.
* **Superclass and Subclass:** Understanding the parent-child relationship in classes.
* **Built-in functions:** Usage of `isinstance`, `issubclass`, `type`, and `super`.
* **Method Overriding:** How to redefine a method in a subclass.

## Requirements

* Python 3.8.5
* Ubuntu 20.04 LTS
* pycodestyle 2.7

## Files and Descriptions

| Filename | Description |
| -------- | ----------- |
| `0-lookup.py` | Function that returns the list of available attributes and methods of an object. |
| `1-my_list.py` | Class `MyList` that inherits from `list` and includes a method to print sorted elements. |
| `2-is_same_class.py` | Function that returns `True` if the object is exactly an instance of the specified class. |
| `3-is_kind_of_class.py` | Function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class. |
| `4-inherits_from.py` | Function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`. |
| `5-base_geometry.py` | Empty class `BaseGeometry`. |
| `6-base_geometry.py` | Class `BaseGeometry` with a public instance method `area`. |
| `7-base_geometry.py` | Class `BaseGeometry` with an integer validator method. |
| `8-rectangle.py` | Class `Rectangle` that inherits from `BaseGeometry`. |
| `9-rectangle.py` | Class `Rectangle` with area implementation and print behavior. |
| `10-square.py` | Class `Square` that inherits from `Rectangle`. |
| `11-square.py` | Class `Square` with size implementation and print behavior. |

## Author

Bernis