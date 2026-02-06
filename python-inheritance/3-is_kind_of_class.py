#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function to check instance or inheritance.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.
    
    Args:
        obj: The object to check.
        a_class: The class to match.
    """
    # isinstance vérifie toute la lignée familiale
    return isinstance(obj, a_class)