#!/usr/bin/python3
"""
Module 11-square
Defines class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square using Rectangle.
    """

    def __init__(self, size):
        """
        Intializes a new Square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the print() and str() representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)