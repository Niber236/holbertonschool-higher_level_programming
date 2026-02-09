#!/usr/bin/python3
"""
Module to serialize and deserialize using XML.
"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.
    """
    # 1. On crée la racine <data>
    root = ET.Element("data")
    
    # 2. On ajoute chaque clé/valeur comme un enfant
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML stocke tout en texte
    
    # 3. On écrit l'arbre dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8')

def deserialize_from_xml(filename):
    """
    Deserializes an XML file to a Python dictionary.
    """
    # 1. On parse le fichier
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # 2. On reconstruit le dictionnaire
        result = {}
        for child in root:
            result[child.tag] = child.text
            
        return result
    except Exception:
        return None
