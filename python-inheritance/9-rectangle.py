#!/usr/bin/python3
"""
Module 9-rectangle
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
        """
        # On valide et on cache les variables (comme avant)
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        # On calcule l'aire avec les variables privées
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the print() and str() representation of the Rectangle.
        """
        # On formate le message : [Rectangle] largeur/hauteur
        return "[Rectangle] {}/{}".format(self.__width, self.__height)