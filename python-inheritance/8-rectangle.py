#!/usr/bin/python3
"""
Module 8-rectangle
Defines class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Intializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # 1. On utilise le validateur du parent POUR la width
        self.integer_validator("width", width)
        # 2. Si ça passe, on stocke en PRIVE (__)
        self.__width = width

        # 3. On fait pareil pour la height
        self.integer_validator("height", height)
        self.__height = height