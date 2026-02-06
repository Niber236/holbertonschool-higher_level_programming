#!/usr/bin/python3
"""
Module 7-base_geometry
This module defines a class BaseGeometry.
It serves as a base class for other geometry classes.
It contains methods for area calculation and integer validation.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    This class contains public instance methods:
    - area: raises an exception when called.
    - integer_validator: validates that a value is a positive integer.
    """

    def area(self):
        """
        Computes the area of the geometry.
        
        Raises:
            Exception: Because this method is not implemented in the
            base class and should be overridden by subclasses.
            The message is always 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
