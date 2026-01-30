#!/usr/bin/python3
"""
Module 2-rectangle: Définit un rectangle avec aire et périmètre.
"""


class Rectangle:
    """
    Classe définissant un rectangle.
    """

    def __init__(self, width=0, height=0):
        """ Init """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Retourne l'aire du rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Retourne le périmètre du rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
