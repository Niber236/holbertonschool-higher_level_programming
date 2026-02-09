#!/usr/bin/python3
"""
Module to convert CSV to JSON using serialization.
"""
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and writes the data to data.json as JSON.
    Returns True if successful, False if file not found.
    """
    try:
        # 1. On ouvre et on lit le CSV
        with open(csv_filename, 'r', encoding='utf-8') as csvf:
            # DictReader transforme chaque ligne en dictionnaire automatiquement
            csvReader = csv.DictReader(csvf)
            # On convertit tout ça en une liste de dictionnaires
            data = list(csvReader)

        # 2. On écrit le résultat dans data.json
        with open('data.json', 'w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf)
            
        return True
    except FileNotFoundError:
        return False
