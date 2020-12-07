import calendar
import os 

from flask_appbuilder import ModelView, AppBuilder, expose, BaseView, has_access
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app import appbuilder
from . import appbuilder, db
from .models import Users , Reset_requests, Clients, Fournisseurs, Entrepots, Expedition_clients, Commandes_fournisseurs#, Operations_internes
 
##Forms
from wtforms import Form, StringField, FileField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from flask import flash, request
from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _

from . import backend as tms

import folium
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

## Traject oprimisation
# class Optimise_traject():

# test
class MyTestView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        # do something with param1
        # and render template with param
        param1= "test variable" #str(test_variable) # used for debuging
        param1 = str(user.data)
        self.update_redirect()
        return self.render_template('dash.html', param1= param1)


class BaseOptimisationView(BaseView):

    default_view = 'optimise'

    @expose('/optimise/')
    @has_access
    def optimise(self):
        # do something with param1
        # and render template with param
        if user.data==None:
            user.set_data("app\data (1).csv","csv")
        if user.mtd==None:
            user.set_methode("vns")
        user.run_optimisation()
        user.get_optimisation()
        user.render_map()
        param1 = str(user.get_optimisation())
        self.update_redirect()
        return self.render_template('optimisation.html' ,param1= param1)


class BaseBalayedOptimisationView(BaseView):
    default_view = 'blayed_optimise'

    @expose('/blayed_optimise/')
    @has_access
    def blayed_optimise(self):
        # do something with param1
        # and render template with param
        if user.data==None:
            user.set_data("app\data (1).csv","csv")
        if user.mtd==None:
            mtd = 1
        user.set_capacity(112)
        user.run_balayage(1)
        user.get_optimisation()
        user.render_map_balay()
        param1 = str(user.get_optimisation())
        self.update_redirect()
        return self.render_template('optimisation.html' ,param1= param1)




class UserOptimisationView(BaseOptimisationView):
    pass

class AdminOptimisationView(BaseOptimisationView):
    pass


class MyMapView(BaseView):
    default_view = 'get_map'

    @expose('/get_map')
    @has_access
    def get_map(self):
        m = user.map
        m.save('app/templates/map.html')
        return self.render_template('map.html')


    

## CSV Upload




class MyForm(DynamicForm):
    field1 = StringField(('Name'),
        description=('name your entry'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())
    
    csv_client = FileField(u'clients csv') #, [validators.regexp(u'^[^/\\]\.csv$')]
    
    csv_expedition = FileField(u'expedition csv') #, [validators.regexp(u'^[^/\\]\.csv$')]
    
    # def validate_image(form, field):
    #     if field.data:
    #         field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)


class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'This is my first form view'
    message = 'My form submitted'

    # def form_get(self, form):
    #     form.field1.data = 'This was prefilled'

    def form_post(self, form):
        # post process form
        # flash(self.message, 'info')
        # upload_path = "uploads/" + str(form.field1.name)
        if form.csv_client.data:
            csv_data = request.files[form.csv_client.name].read()
            flash(self.message, 'csv clients')
            print(csv_data)
            user.set_data_bytes(csv_data, separetor=',')
        if form.csv_expedition.data:
            csv_data2 = request.files[form.csv_expedition.name].read()
            flash(self.message, 'csv expeditions')
            print("csv data2 {{{{{{{{{{{{{{{{{")
            print(csv_data2)
            user.set_expedition_data(csv_data2, separetor=',')
        






###initiating the db


db.create_all()

user = tms.Tms_User("Zakaria")

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


##CSV
appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
                     category="My Forms", category_icon="fa-cogs")


appbuilder.add_view(MyTestView, "test", category="testViews")
appbuilder.add_view(UserOptimisationView, "optimise", category="User")
appbuilder.add_view(AdminOptimisationView, "optimise", category="admin")


appbuilder.add_view(MyMapView, "map", category="testViews" )
appbuilder.add_view(BaseBalayedOptimisationView, "BaseBalayedOptimisationView", category="testViews" )
# appbuilder.add_view(DashView, "Tableau de bord", category='Dashboard')