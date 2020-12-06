import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

mindate = datetime.date(datetime.MINYEAR, 1, 1)



### my classes
class Users(Model):
    id = Column(Integer, primary_key=True)
    username= Column(String(50), unique=True, nullable=False)
    password= Column(String(50),  nullable=False)
    typee= Column(String(50),  nullable=False)
    
    def __repr__(self):
        return self.username


class Reset_requests(Model):
    id = Column(Integer, primary_key=True)
    user=Column(String(50),  ForeignKey("users.username"), nullable=False)
    users = relationship(Users)
    request_state=Column(String(50),  nullable=False)


class Clients(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), unique=True, nullable=False)
    adresse=Column(String(50),  nullable=False)
    email=Column(String(50), unique=True, nullable=False)
    phone_number=Column(String(50), unique=True, nullable=False)
    longitude=Column(String(50),  nullable=False)
    latitude=Column(String(50),  nullable=False)
    
    def __repr__(self):
        return self.full_name
   
    
class Fournisseurs(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), unique=True, nullable=False)
    adresse=Column(String(50),  nullable=False)
    email=Column(String(50), unique=True, nullable=False)
    phone_number=Column(String(50), unique=True, nullable=False)
    longitude=Column(String(50), nullable=False)
    latitude=Column(String(50), nullable=False)
    
    def __repr__(self):
        return self.full_name


class Entrepots(Model):
    id = Column(Integer, primary_key=True)
    adress=Column(String(50),  nullable=False)
    email=Column(String(50), unique=True, nullable=False)
    longitude=Column(String(50), nullable=False)
    latitude=Column(String(50),  nullable=False)
    

    def __repr__(self):
        return self.adress


class Expedition_clients(Model):
    id = Column(Integer, primary_key=True)
    ent_origine = Column(Integer,  ForeignKey("entrepots.id"), nullable=False)
    entrepots = relationship(Entrepots)
    client=Column(Integer, ForeignKey("clients.id"), nullable=False)
    clients = relationship(Clients)
    quantity = Column(String(50), nullable=True)
    delivery_date=Column(Date, nullable=True)
    Shipping_costs=Column(Integer, nullable=False)
    delivery_state=Column(String(50),  nullable=False)
    
    def __repr__(self):
        return self.id
 

class Commandes_fournisseurs(Model):
    id = Column(Integer, primary_key=True)
    fournisseur=Column(Integer,  ForeignKey("fournisseurs.id"), nullable=False)
    fournisseurs = relationship(Fournisseurs )
    eny_dest=Column(Integer,  ForeignKey("entrepots.id"), nullable=False)
    entrepots = relationship(Entrepots)
    shiping_date=Column(Date, nullable=True)
    Shiping_costs=Column(Integer,  nullable=False)
    delivery_state=Column(String(50),  nullable=False)
    
    def __repr__(self):
        return self.id


# class Operations_internes(Model):
#     id = Column(Integer, primary_key=True)
#     ent_origine = Column(Integer,  ForeignKey("entrepots1.id"), nullable=False)
#     entrepots1 = relationship(Entrepots, primaryjoin="Entrepots")
#     client=Column(Integer, ForeignKey("entrepots2.id"), nullable=False)
#     entrepots2 = relationship(Entrepots)
#     delivery_date=Column(Date, nullable=True)
#     Shiping_costs=Column(Integer, nullable=False)
#     order_state=Column(String(50), unique=True, nullable=False)
    
#     def __repr__(self):
#         return self.id