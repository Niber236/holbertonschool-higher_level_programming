#!/usr/bin/python3
"""
Module 2-is_same_class
Defines a function to check exact class equality.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.
    
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    """
    # On compare le type de l'objet directement avec la classe
    return type(obj) is a_class
