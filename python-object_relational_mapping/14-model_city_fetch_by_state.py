#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Connexion au serveur
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # On requête les deux tables et on les lie par l'ID
    query = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()
    
    # On affiche au format demandé : <state name>: (<city id>) <city name>
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
        
    session.close()