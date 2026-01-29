#!/usr/bin/python3
"""
Module 5-square: Définit un carré avec affichage.
"""


class Square:
    """
    Classe définissant un carré.
    """

    def __init__(self, size=0):
        """
        Initialise le carré.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter : Récupère la taille.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter : Modifie la taille avec validation.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l'aire du carré.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche le carré avec le caractère #.
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)