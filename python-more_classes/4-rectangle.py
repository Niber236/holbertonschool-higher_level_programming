#!/usr/bin/python3
"""
Module 4-rectangle: Définit un rectangle avec __str__ et __repr__.
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
        """ Aire """
        return self.width * self.height

    def perimeter(self):
        """ Périmètre """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        Retourne la représentation visuelle (#).
        """
        if self.width == 0 or self.height == 0:
            return ""
        
        rect = []
        for i in range(self.height):
            rect.append("#" * self.width)
        return "\n".join(rect)

    def __repr__(self):
        """
        Retourne la représentation officielle (code pour recréer l'objet).
        Format: Rectangle(width, height)
        """
        return "Rectangle({}, {})".format(self.width, self.height)
    