import calendar

from flask_appbuilder import ModelView
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Users , Reset_requests, Clients, Fournisseurs, Entrepots, Expedition_clients, Commandes_fournisseurs#, Operations_internes



### my stuff


## Admi's Views
class UsersModelView(ModelView):
    datamodel = SQLAInterface(Users)

class Reset_requestsModelView(ModelView):
    datamodel = SQLAInterface(Reset_requests)
    related_views = [UsersModelView]

class ClientsModelView(ModelView):
    datamodel = SQLAInterface(Clients)

class FournisseursModelView(ModelView):
    datamodel = SQLAInterface(Fournisseurs)

class EntrepotsModelView(ModelView):
    datamodel = SQLAInterface(Entrepots)

class Expedition_clientsModelView(ModelView):
    datamodel = SQLAInterface(Expedition_clients)
    related_views = [EntrepotsModelView,ClientsModelView]

class Commandes_fournisseursModelView(ModelView):
    datamodel = SQLAInterface(Commandes_fournisseurs)
    related_views = [EntrepotsModelView,FournisseursModelView]

# class Operations_internesModelView(ModelView):
#     datamodel = SQLAInterface(Operations_internes)
#     related_views = [EntrepotsModelView]


## User's Views

class User_ClientsModelView(ModelView):
    datamodel = SQLAInterface(Clients)

class User_FournisseursModelView(ModelView):
    datamodel = SQLAInterface(Fournisseurs)

class User_EntrepotsModelView(ModelView):
    datamodel = SQLAInterface(Entrepots)

class User_Expedition_clientsModelView(ModelView):
    datamodel = SQLAInterface(Expedition_clients)
    related_views = [User_EntrepotsModelView,User_ClientsModelView]

class User_Commandes_fournisseursModelView(ModelView):
    datamodel = SQLAInterface(Commandes_fournisseurs)
    related_views = [User_EntrepotsModelView,User_FournisseursModelView]

##client's Views

class Client_Expedition_clientsModelView(ModelView):
    datamodel = SQLAInterface(Expedition_clients)
    related_views = [User_EntrepotsModelView,User_ClientsModelView]

#### chart stuff


###initiating the db

db.create_all()


### generating the views

### my views

#Admin
appbuilder.add_view(
    UsersModelView,             "Users test",       category="admin",   category_icon="fa-admin",
)
appbuilder.add_view(
    Reset_requestsModelView,             "Reset_requests",       category="admin"
)
appbuilder.add_view(
    ClientsModelView,             "Clients",       category="admin"
)
appbuilder.add_view(
    FournisseursModelView,             "Fournisseurs",       category="admin"
)
appbuilder.add_view(
    EntrepotsModelView,             "Entrepots",       category="admin"
)
appbuilder.add_view(
    Expedition_clientsModelView,             "Expedition Clients",       category="admin"
)
appbuilder.add_view(
    Commandes_fournisseursModelView,             "Commandes fournisseurs",       category="admin"
)

# appbuilder.add_view(
#     Operations_internesModelView,             "Operation internes",       category="admin"
# )

##User
appbuilder.add_view(
    User_ClientsModelView,             "Clients",       category="User",   category_icon="fa-admin",
)
appbuilder.add_view(
    User_FournisseursModelView,             "Fournisseurs",       category="User"
)
appbuilder.add_view(
    User_EntrepotsModelView,             "Entrepots",       category="User"
)
appbuilder.add_view(
    User_Expedition_clientsModelView,             "Expedition Clients",       category="User"
)
appbuilder.add_view(
    User_Commandes_fournisseursModelView,             "Commandes fournisseurs",       category="User"
)

##Client
appbuilder.add_view(
    Client_Expedition_clientsModelView,             "Expedition Clients",       category="Client"
)
