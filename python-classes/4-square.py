#!/usr/bin/python3
"""
Module 4-square: Définit un carré avec Getters et Setters.
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
        # SUBTILITÉ : On appelle le setter ici !
        # On n'écrit pas self.__size = size direct.
        # On écrit self.size = size pour forcer la validation immédiate.
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
        Args:
            value (int): La nouvelle taille.
        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
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