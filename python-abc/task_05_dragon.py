#!/usr/bin/env python3

class SwimMixin:
    """
    Mixin qui ajoute la capacité de nager.
    """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """
    Mixin qui ajoute la capacité de voler.
    """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Classe Dragon qui hérite des capacités de nage et de vol via les Mixins.
    """
    def roar(self):
        print("The dragon roars!")