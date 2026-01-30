#!/usr/bin/python3
"""
Module 6-rectangle: Définit un rectangle avec compteur d'instances.
"""


class Rectangle:
    """
    Classe définissant un rectangle.
    Attributs de classe:
        number_of_instances (int): Le nombre d'instances actives.
    """

    # C'est ICI qu'on déclare le compteur (hors des fonctions)
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Init """
        self.width = width
        self.height = height
        # À chaque naissance, on incrémente le compteur GLOBAL
        Rectangle.number_of_instances += 1

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
        """ Représentation visuelle """
        if self.width == 0 or self.height == 0:
            return ""
        
        rect = []
        for i in range(self.height):
            rect.append("#" * self.width)
        return "\n".join(rect)

    def __repr__(self):
        """ Représentation officielle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Décrémente le compteur et affiche un message.
        """
        # À chaque mort, on décrémente le compteur GLOBAL
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
