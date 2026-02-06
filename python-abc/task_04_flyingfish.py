#!/usr/bin/env python3

class Fish:
    """
    Classe représentant un poisson.
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe FlyingFish qui hérite de Fish ET de Bird.
    Elle écrase (override) les méthodes de ses parents.
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")