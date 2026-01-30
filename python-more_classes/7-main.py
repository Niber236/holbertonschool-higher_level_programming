#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")

# Changement global pour TOUS les rectangles à venir
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2) # Lui utilise le défaut (#) car on a changé l'instance 1, pas la classe
print("--")

# Changement GLOBAL au niveau de la classe
Rectangle.print_symbol = "C"
print(my_rectangle_2) # Maintenant il utilise C
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3) # Lui aussi utilise C par défaut
print("--")

# L'instance 1 garde son symbole perso (&) car elle a "shadowed" la classe
print(my_rectangle_1)
print("--")