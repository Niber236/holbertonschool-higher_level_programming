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

        Args:
            name: The name of the value (string).
            value: The value to validate (int).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        # 1. Vérification du Type (On veut un int pur)
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        # 2. Vérification de la Valeur (Strictement positive)
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))