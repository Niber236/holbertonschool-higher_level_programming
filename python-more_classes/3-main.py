#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(4, 2)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle)) # Ça affiche encore l'adresse mémoire pour l'instant

print("--")

my_rectangle.width = 3
my_rectangle.height = 3
print(my_rectangle)

print("--")

my_rectangle.width = 3
my_rectangle.height = 0
print(my_rectangle)

print("--")