#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function to check if object is an instance of a subclass.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    
    Args:
        obj: The object to check.
        a_class: The class to match.
    """
    # 1. On vérifie s'il appartient à la famille (isinstance)
    # 2. ET on vérifie qu'il n'est PAS exactement de ce type (type is not)
    return isinstance(obj, a_class) and type(obj) is not a_class