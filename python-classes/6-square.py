#!/usr/bin/python3
"""
Module 6-square: Définit un carré avec taille, position et affichage.
"""


class Square:
    """
    Classe définissant un carré.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise le carré.
        Args:
            size (int): Taille du côté.
            position (tuple): Coordonnées (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter taille """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter taille """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter position """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter position avec validation STRICTE.
        Doit être un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calcule l'aire """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche le carré en prenant en compte la position.
        """
        if self.size == 0:
            print("")
            return

        # 1. Gérer la position Y (Lignes vides au dessus)
        # On imprime 'position[1]' fois une ligne vide
        [print("") for i in range(self.position[1])]

        # 2. Gérer la position X (Espaces à gauche) + Le carré
        for i in range(self.size):
            # On imprime 'position[0]' espaces, PUIS les '#'
            print(" " * self.position[0] + "#" * self.size)