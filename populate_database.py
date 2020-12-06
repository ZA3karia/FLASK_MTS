

from app import db
# from app.models import Clients, Entrepots, Expedition_clients  #, Commandes_fournisseurs#, Operations_internes

from sqlalchemy.types import Integer, Text, String, DateTime

import os

import pandas as pd
from os import environ
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)


client_data = pd.read_csv("generated data\Clients.csv", sep=',')
entropot_data = pd.read_csv("generated data\Entrepos.csv", sep=',')
expedition_data = pd.read_csv("generated data\Expeditions.csv", sep=',')


client_table_name = "clients"
client_data.to_sql(
    client_table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    ### csv header
    #id,full_name,adresse,email,phone_number,longitude,latitude
    ### database header
    # id = Column(Integer, primary_key=True)
    # full_name = Column(String(50), unique=True, nullable=False)
    # adresse=Column(String(50),  nullable=False)
    # email=Column(String(50), unique=True, nullable=False)
    # phone_number=Column(String(50), unique=True, nullable=False)
    # longitude=Column(String(50),  nullable=False)
    # latitude=Column(String(50),  nullable=False)
    
    dtype={
        "id": Integer,
        "full_name": String(50),
        "adresse": String(50),
        "email":  String(50),
        "phone_number": String(50),
        "longitude": String(50),
        "latitude": String(50)
    }
)


entropot_table_name = "_Entrepots"
entropot_data.to_sql(
    entropot_table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    ### csv header
    # id,adress,email,longitude,latitude
    ### database header
    # id = Column(Integer, primary_key=True)
    # adresse=Column(String(50),  nullable=False)
    # email=Column(String(50), unique=True, nullable=False)
    # longitude=Column(String(50), nullable=False)
    # latitude=Column(String(50),  nullable=False)
    
    dtype={
        "id": Integer,
        "adress": String(50),
        "email": String(50),
        "longitude":  String(50),
        "latitude": String(50)
    }
)

expedition_table_name = "Expedition_clients"
client_data.to_sql(
    expedition_table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    ### csv header
    # id,ent_origine,client,quantity,delivery_date,shipping_costs,delivery_state
    ### database header
    # id = Column(Integer, primary_key=True)
    # ent_origine = Column(Integer,  ForeignKey("entrepots.id"), nullable=False)
    # --entrepots = relationship(Entrepots)
    # client=Column(Integer, ForeignKey("clients.id"), nullable=False)
    # --clients = relationship(Clients)
    # quantity = Column(String(50), nullable=True)
    # delivery_date=Column(Date, nullable=True)
    # shipping_costs=Column(Integer, nullable=False)
    # delivery_state=Column(String(50),  nullable=False)
    
    dtype={
        "id": Integer,
        "ent_origine": Integer,
        "client": Integer,
        "quantity":  String(50),
        "delivery_date": DateTime,
        "shipping_costs": Integer,
        "delivery_state": String(50)
    }
)