#!/usr/bin/env python3

class CountedIterator:
    """
    Un itérateur qui compte le nombre d'éléments itérés.
    """

    def __init__(self, some_iterable):
        """
        Initialise l'itérateur avec un itérable (liste, tuple, etc.)
        et met le compteur à 0.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        Retourne le nombre d'éléments itérés jusqu'à présent.
        """
        return self.counter

    def __next__(self):
        """
        Surcharge de la méthode __next__.
        Récupère l'élément suivant, incrémente le compteur, et renvoie l'élément.
        Si c'est la fin, renvoie l'exception StopIteration.
        """
        try:
            # On tente de récupérer le suivant
            item = next(self.iterator)
            # Si ça marche, on incrémente
            self.counter += 1
            return item
        except StopIteration:
            # Si c'est fini, on relève l'exception pour arrêter la boucle
            raise StopIteration
            
    def __iter__(self):
        """
        Rend la classe itérable elle-même.
        """
        return self