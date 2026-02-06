#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
# True est un booléen. bool hérite de int.
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

# True est un booléen. C'est exactement la classe bool.
# Donc ici, ça doit renvoyer False (car on veut seulement les héritiers).
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))

# True est un objet. bool hérite de object.
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))