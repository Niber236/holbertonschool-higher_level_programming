#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    
    # La requête SQL avec la jointure et le bouclier %s
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    
    # On exécute en passant l'argument de l'utilisateur (sécurisé)
    cur.execute(query, (sys.argv[4],))
    
    rows = cur.fetchall()
    
    # On extrait le nom (row[0]) de chaque ligne et on les colle avec ", "
    print(", ".join([row[0] for row in rows]))
    
    cur.close()
    db.close()