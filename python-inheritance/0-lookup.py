#!/usr/bin/python3
"""
Module 0-lookup
Définit une fonction qui liste les attributs d'un objet.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet.
    """
    return dir(obj)