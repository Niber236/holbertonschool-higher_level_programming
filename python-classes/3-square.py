#!/usr/bin/python3
"""
Module 3-square: Définit un carré avec validation et calcul d'aire.
"""


class Square:
    """
    Classe définissant un carré.
    """

    def __init__(self, size=0):
        """
        Initialise le carré.
        Args:
            size (int): Taille du côté (défaut 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcule l'aire du carré.
        Returns:
            L'aire (taille * taille).
        """
        return self.__size * self.__size