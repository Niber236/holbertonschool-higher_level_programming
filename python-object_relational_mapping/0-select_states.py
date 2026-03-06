#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # On ouvre la porte de la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # On crée un "curseur", c'est le bras mécanique qui va exécuter le SQL
    cur = db.cursor()

    # On balance la requête SQL pure
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # On récupère toutes les lignes et on les affiche une par une
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # On nettoie derrière nous
    cur.close()
    db.close()