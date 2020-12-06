import logging
from app import db
from app.models import Clients, Entrepots, Expedition_clients  #, Commandes_fournisseurs#, Operations_internes
from sqlalchemy.types import Integer, Text, String, DateTime


import pandas as pd

log = logging.getLogger(__name__)

client_data = pd.read("generated data\Clients.csv", sep=',')
entropot_data = pd.read("generated data\Entrepos.csv", sep=',')
expedition_data = pd.read("generated data\Expeditions.csv", sep=',')


client_data.to_sql()