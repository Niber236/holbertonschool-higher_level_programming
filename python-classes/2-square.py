#!/usr/bin/python3
"""
Ce module définit une classe Square avec validation.
"""


class Square:
    """
    Classe qui définit un carré.
    """

    def __init__(self, size=0):
        """
        Initialise un nouveau carré.

        Args:
            size (int): La taille du carré. Par défaut 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        