import os
from flask import Flask, render_template
from flask_appbuilder import SQLA, AppBuilder, AppBuilder, expose, BaseView, has_access
from flask_bootstrap import Bootstrap

from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm


class MyForm(DynamicForm):
    field1 = StringField(('Field1'),
        description=('Your field number one!'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())
    field2 = StringField(('Field2'),
        description=('Your field number two!'), widget=BS3TextFieldWidget())

# init Flask
app = Flask(__name__)
Bootstrap(app)
def index():
    return render_template('methode3.html')
# Basic config with security for forms and session cookie
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'thisismyscretkey'
# database altered
# Init SQLAlchemy
db = SQLA(app)
# Init F.A.B.
appbuilder = AppBuilder(app, db.session)


#creating the views
class MyView(BaseView):
########################          ESPACE ADMIN          ############################
    default_view = 'AccueilAdmin'

    ##########          TABLEAU DE BORD         ############
    @expose('/AccueilAdmin/')
    @has_access
    def AccueilAdmin(self):
        # do something with param1
        # and return to previous page or index
        
        self.update_redirect()
        return self.render_template('tableaudebord.html')

    ##########          FONCTIONNALITÉS         ############

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('fonctionnalités.html',
                            param1 = param1)


    @expose('/method100/<string:param1>')
    @has_access
    def method100(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('login.html',
                            param1 = param1)



    ##########          CREER UN COMPTE         ############
    @expose('/creercompte/<string:param1>')
    @has_access
    def method4(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('creercompte.html',
                            param1 = param1)
########################          ESPACE UTILISATEUR         ############################

    ##########          ACCUEIL UTILISATEUR        ############
    view = 'utilisateur'
    @expose('/index/')
    @has_access
    def index(self):
        # do something with param1
        # and return to previous page or index
        
        self.update_redirect()
        return self.render_template('login.html')

    ##########          LOGIN UTILISATEUR        ############

    @expose('/Fonctionnalités/<string:param1>')
    @has_access
    def method3(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('index.html',
                            param1 = param1)



########################          ESPACE ADMIN          ############################
#accueil admin tableau de bord
appbuilder.add_view(MyView, "Accueil Admin", category='Espace Admin')

appbuilder.add_link("Method2", href='/myview/method2/john', category='Espace Admin')
appbuilder.add_link("Fonctionnalités", href='/myview/Fonctionnalités/john', category='Espace Admin')
appbuilder.add_link("login form", href='/myview/method100/john', category='Espace Admin')
appbuilder.add_link("Créer un compte", href='/myview/creercompte/john', category='Espace Admin')

########################          ESPACE UTILISATEUR          ############################

appbuilder.add_link("index", href='/myview/index/john', category='Espace utilisateur')

########################          ESPACE CLIENT          ############################

appbuilder.add_link("Method2", href='/myview/method2/john', category='Espace Client')




        



# Run the development server
app.run(debug=True)
