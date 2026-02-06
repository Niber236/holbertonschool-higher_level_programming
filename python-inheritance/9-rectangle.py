#!/usr/bin/python3
"""
Module 9-rectangle
This module defines a class Rectangle that inherits from BaseGeometry.
It includes methods for initialization, area calculation, and string representation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.
    Inherits from BaseGeometry and adds width/height validation.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle. Must be positive.
            height (int): The height of the rectangle. Must be positive.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the Rectangle.
        
        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the informal string representation of the Rectangle.
        
        Returns:
            str: A string in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)