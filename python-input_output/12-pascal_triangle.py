#!/usr/bin/python3
"""
Module 12-pascal_triangle
Contains a function that returns a list of lists of integers representing the Pascal's triangle of n.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # On commence une ligne remplie de 1, de longueur i + 1
        # Exemple ligne 2 (i=2) -> [1, 1, 1] (on va modifier le milieu après)
        row = [1] * (i + 1)
        
        # On calcule les valeurs du milieu (si i > 1)
        if i > 1:
            for j in range(1, i):
                # La valeur est la somme des deux valeurs au-dessus (ligne i-1)
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle.append(row)
        
    return triangle
