#!/usr/bin/python3
"""
Module 11-square
This module defines a class Square that inherits from Rectangle.
It specifically handles squares where width equals height.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square geometry.
    Inherits from Rectangle since a square is a special rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.
        
        Args:
            size (int): The size of the square's sides. Must be positive.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the Square.
        
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the informal string representation of the Square.
        
        Returns:
            str: A string in the format [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)