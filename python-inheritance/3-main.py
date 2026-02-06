#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
# 1 est un entier
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))

# 1 est un float ? NON.
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))

# 1 est un objet ? OUI (car tout hérite d'object) -> C'est la différence avec Task 2 !
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))