#!/usr/bin/python3
"""
Module 9-rectangle: Définit un rectangle avec méthode de classe 'square'.
"""


class Rectangle:
    """
    Classe définissant un rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Init """
        self.width = width
        self.height = height
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
        symbol = str(self.print_symbol)
        for i in range(self.height):
            rect.append(symbol * self.width)
        return "\n".join(rect)

    def __repr__(self):
        """ Représentation officielle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Décrémente compteur """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compare deux rectangles (statique) """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Crée un nouveau Rectangle avec width == height == size.
        Args:
            size (int): La taille du carré.
        Returns:
            Une nouvelle instance de Rectangle.
        """
        # On appelle cls(...) ce qui revient à faire Rectangle(...)
        return cls(size, size)
