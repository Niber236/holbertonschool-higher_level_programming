#!/usr/bin/env python3

class NoPylist(list):
    """
    Une liste personnalisée qui n'accepte que des entiers.
    Elle hérite de la classe native 'list'.
    """

    def append(self, item):
        """
        Ajoute un élément à la liste uniquement si c'est un entier.
        Sinon, lève une TypeError.
        """
        if isinstance(item, int):
            # On utilise super() pour appeler la VRAIE méthode append de list
            super().append(item)
        else:
            raise TypeError("Only integers can be added")