#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi

# 1. La Classe Abstraite (Le Contrat)
class Shape(ABC):
    """ Classe abstraite Shape """
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# 2. Les Classes Concrètes (Les Enfants)
class Circle(Shape):
    """ Implémentation d'un Cercle """
    
    def __init__(self, radius):
        # On peut mettre radius en négatif car l'énoncé ne demande pas de validation ici
        # Mais dans la vraie vie, on validerait abs(radius)
        self.radius = abs(radius)

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    """ Implémentation d'un Rectangle """
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 3. Le Duck Typing (La Fonction Magique)
def shape_info(shape):
    """
    Affiche l'aire et le périmètre.
    Cette fonction s'en fiche que l'objet soit un Rectangle ou un Cercle.
    Elle veut juste que l'objet ait les méthodes .area() et .perimeter().
    C'est ça le Duck Typing : "Si ça marche comme un canard, c'est un canard".
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))