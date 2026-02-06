#!/usr/bin/env python3

class VerboseList(list):
    """
    Une classe qui hérite de 'list' et qui notifie
    l'utilisateur lors des modifications (ajout/suppression).
    """

    def append(self, item):
        """
        Ajoute un item à la fin et affiche une notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """
        Étend la liste avec plusieurs items et affiche une notification.
        """
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """
        Supprime un item et affiche une notification avant la suppression.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Retire un item à un index donné (défaut dernier) et notifie avant.
        """
        # On récupère l'objet pour pouvoir l'afficher dans le message
        # Note : Si l'index est invalide, self[index] lèvera l'erreur, ce qui est le comportement attendu.
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)