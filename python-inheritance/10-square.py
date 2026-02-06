#!/usr/bin/python3
"""
Module 10-square
Defines class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square using Rectangle.
    """

    def __init__(self, size):
        """
        Intializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        # 1. On valide la size avec le validateur du Grand-Père (BaseGeometry)
        self.integer_validator("size", size)
        
        # 2. On stocke la size en privé
        self.__size = size
        
        # 3. LE TRUC MALIN : On appelle le constructeur du Père (Rectangle)
        # On lui dit : "Je suis un rectangle de largeur=size et hauteur=size"
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        # Techniquement, Rectangle.area() marcherait déjà, 
        # mais c'est plus propre de le redéfinir ici avec la formule du carré.
        return self.__size ** 2