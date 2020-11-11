import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

mindate = datetime.date(datetime.MINYEAR, 1, 1)

class Users(Model):
    id = Column(Integer, primary_key=True)
    username= Column(String(50), unique=True, nullable=False)
    password= Column(String(50), unique=True, nullable=False)
    typee= Column(String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return self.username

class Reset_requests(Model):
    id = Column(Integer, primary_key=True)
    user=Column(String(50),  ForeignKey("users.username"), nullable=False)
    request_state=Column(String(50), unique=True, nullable=False)


class Clients(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), unique=True, nullable=False)
    adresse=Column(String(50), unique=True, nullable=False)
    email=Column(String(50), unique=True, nullable=False)
    phone_number=Column(String(50), unique=True, nullable=False)
    longitude=Column(String(50), unique=True, nullable=False)
    latitude=Column(String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return self.full_name

   
    
class Fournisseurs(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), unique=True, nullable=False)
    adresse=Column(String(50), unique=True, nullable=False)
    email=Column(String(50), unique=True, nullable=False)
    phone_number=Column(String(50), unique=True, nullable=False)
    longitude=Column(String(50), unique=True, nullable=False)
    latitude=Column(String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return self.full_name

    



class Entrepos(Model):
    id = Column(Integer, primary_key=True)
    adresse=Column(String(50), unique=True, nullable=False)
    email=Column(String(50), unique=True, nullable=False)
    longitude=Column(String(50), unique=True, nullable=False)
    latitude=Column(String(50), unique=True, nullable=False)
    

    def __repr__(self):
        return self.adresse

class Expedition_clients(Model):
    id = Column(Integer, primary_key=True)
    ent_origine = Column(Integer,  ForeignKey("entrepots.id"), nullable=False)
    client=Column(Integer, ForeignKey("entrepots.id"), nullable=False)
    delivery_date=Column(Date, nullable=True)
    Shiping_costs=Column(Integer, nullable=False)
    order_state=Column(String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return self.id
    

   


class Commandes_fournisseurs(Model):
    id = Column(Integer, primary_key=True)
    fournisseur=Column(Integer,  ForeignKey("fournisseurs.id"), nullable=False)
    eny_dest=Column(Integer,  ForeignKey("entrepots.id"), nullable=False)
    shiping_date=Column(Date, nullable=True)
    Shiping_costs=Column(Integer,  nullable=False)
    order_state=Column(String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return self.id

    

class Operations_internes(Model):
    id = Column(Integer, primary_key=True)
    ent_origine = Column(Integer,  ForeignKey("entrepots.id"), nullable=False)
    client=Column(Integer, ForeignKey("entrepots.id"), nullable=False)
    delivery_date=Column(Date, nullable=True)
    Shiping_costs=Column(Integer, nullable=False)
    order_state=Column(String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return self.id