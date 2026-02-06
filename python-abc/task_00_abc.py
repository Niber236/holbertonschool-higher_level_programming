#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Classe abstraite Animal.
    Elle ne peut PAS être instanciée directement.
    """
    @abstractmethod
    def sound(self):
        """ Méthode abstraite que les enfants DOIVENT implémenter """
        pass

class Dog(Animal):
    """ Sous-classe Dog """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """ Sous-classe Cat """
    def sound(self):
        return "Meow"