#!/usr/bin/python3
"""
Module 7-base_geometry
Defines class BaseGeometry with area and integer_validator methods.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))