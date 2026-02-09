#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file.
"""
import sys
import os.path

# On importe tes fonctions des tâches précédentes
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []

# Si le fichier existe déjà, on charge son contenu
if os.path.exists(filename):
    my_list = load_from_json_file(filename)

# On ajoute les arguments passés en ligne de commande (sauf le nom du script)
my_list.extend(sys.argv[1:])

# On sauvegarde la nouvelle liste
save_to_json_file(my_list, filename)
