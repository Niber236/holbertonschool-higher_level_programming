#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

# 1. Test des classes concrètes (Ça marche)
bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

# 2. Test de la classe abstraite (Ça DOIT planter)
try:
    animal = Animal()
    print(animal.sound())
except TypeError as e:
    print(e)