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
    return render_template('login.html')
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


    ##########          PREMIERE CONNEXION ADMIN       ############
    @expose('/FirstConnAdmin/<string:param1>')
    @has_access
    def FirstConnAdmin(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('FirstConnAdmin.html',
                            param1 = param1)

    ##########          CREER UN COMPTE  UTILISATEUR       ############
    @expose('/creercompte/<string:param1>')
    @has_access
    def method4(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('creercompte.html',
                            param1 = param1)



    ##########           UTILISATEURS        ############
    @expose('/utilisateurs/<string:param1>')
    @has_access
    def utilisateurs(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('utilisateurs.html',
                            param1 = param1)                           

 ##########          CREER  CLIENT       ############

    @expose('/client/<string:param1>')
    @has_access
    def client(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('client.html',
                            param1 = param1)    

 ##########          FOURNISSEUR       ############

    @expose('/fournisseur/<string:param1>')
    @has_access
    def fournisseur(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('fournisseur.html',
                            param1 = param1)    

 ##########    LIST  FOURNISSEUR       ############

    @expose('/listfournisseur/<string:param1>')
    @has_access
    def listfournisseur(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('listefourn.html',
                            param1 = param1)    
 ##########    CRÉER ENTREPOT       ############

    @expose('/CRentrepot/<string:param1>')
    @has_access
    def CRentrepot(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('creer_entrepot.html',
                            param1 = param1)    
 ##########    ENTREPOT       ############

    @expose('/entrepot/<string:param1>')
    @has_access
    def entrepot(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('entrepot.html',
                            param1 = param1)   

  ##########          DEMANDES CHANGEMENT MDP  USER      ############                           

    @expose('/demandemdp/<string:param1>')
    @has_access
    def demandemdp(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('demandemdp.html',
                            param1 = param1)

 ##########          CRÉER UN CLIENT     ############              
    @expose('/CRclient/<string:param1>')
    @has_access
    def CRclient(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('CRclient.html',
                            param1 = param1)                  
 ##########          COMMANDES FOURNISSEURS    ############              
    @expose('/commF/<string:param1>')
    @has_access
    def commF(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('commF.html',
                            param1 = param1)      
##########         Enregistrement Des Opérations De Transportation Internes  ############              
    @expose('/EnrOppTrans/<string:param1>')
    @has_access
    def EnrOppTrans(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('EnrOppTrans.html',
                            param1 = param1)  
  ##########         CRÉER UNE COMMANDE  ############              
    @expose('/commande/<string:param1>')
    @has_access
    def commande(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('commande.html',
                            param1 = param1)                                    

##################################          ESPACE CLIENT       ############################################################

    @expose('/method100/<string:param1>')
    @has_access
    def method100(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('editpw.html',
                            param1 = param1)



########################          ESPACE UTILISATEUR         ############################

    ##########          FIRST CONN UTILISATEUR        ############
    @expose('/firstconnuser/<string:param1>')
    @has_access
    def firstconnuser(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('firstconnuser.html',
                            param1 = param1)
  
      ##########          CHANGER MOT DE PASSE       ############
  
    @expose('/method1000/<string:param1>')
    @has_access
    def method1000(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('editpw.html',
                            param1 = param1)


##########         OPTIMISATION DES TRAJETS      ############
    @expose('/OptimisationTrajet/<string:param1>')
    @has_access
    def OptimisationTrajet(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('OptimisationTrajet.html',
                            param1 = param1)
 ##########         Gestion DES HANGEMENTS MDP CLIENT      ############

    @expose('/ChangerMDPclient/<string:param1>')
    @has_access
    def ChangerMDPclient(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('ChangerMDPclient.html',
                            param1 = param1)
    ##########          ENREGISTER EXPEDITION CLIENT      ############

    @expose('/exped/<string:param1>')
    @has_access
    def exped(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('exped.html',
                            param1 = param1)
########################          ESPACE CLIENT        ############################

    ##########          SUIVI EXPEDITION        ############
    @expose('/suiviexped/<string:param1>')
    @has_access
    def suiviexped(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('suiviexped.html',
                            param1 = param1)

    ##########          HISTORIQUE EXPEDITION        ############
    @expose('/histexped/<string:param1>')
    @has_access
    def histexped(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('historique_exped.html',
                            param1 = param1)






########################          ESPACE ADMIN          ############################
#accueil admin tableau de bord
appbuilder.add_link("Première connection", href='/myview/FirstConnAdmin/john', category='Espace Admin')
appbuilder.add_view(MyView, "Tableau de bord", category='Espace Admin')
appbuilder.add_link("Utilisateurs", href='/myview/utilisateurs/john', category='Espace Admin')
appbuilder.add_link("Clients", href='/myview/client/john', category='Espace Admin')
appbuilder.add_link("Fournisseurs ", href='/myview/listfournisseur/john', category='Espace Admin')
appbuilder.add_link("Expédition client", href='/myview/exped/john', category='Espace Admin')
appbuilder.add_link("Commandes", href='/myview/commande/john', category='Espace Admin')
appbuilder.add_link("Entrepôt", href='/myview/entrepot/john', category='Espace Admin')
appbuilder.add_link("Opérations De Transportation Internes", href='/myview/EnrOppTrans/john', category='Espace Admin')
appbuilder.add_link("Commandes Fournisseurs", href='/myview/commF/john', category='Espace Admin')
appbuilder.add_link("Gestion des mots de passe", href='/myview/demandemdp/john', category='Espace Admin')
appbuilder.add_link("Modifier le mot de passe", href='/myview/method1000/john', category='Espace Admin')
appbuilder.add_link("Optimisation des trajets", href='/myview/OptimisationTrajet/john', category='Espace Admin')


########################          ESPACE UTILISATEUR          ############################


appbuilder.add_link("Première connexion", href='/myview/firstconnuser/john', category='Espace utilisateur')
appbuilder.add_link("Expédition client", href='/myview/exped/john', category='Espace utilisateur')
appbuilder.add_link("Clients", href='/myview/client/john', category='Espace utilisateur')
appbuilder.add_link("Fournisseurs ", href='/myview/listfournisseur/john', category='Espace utilisateur')
appbuilder.add_link("Opérations De Transportation Internes", href='/myview/EnrOppTrans/john', category='Espace utilisateur')
appbuilder.add_link("Entrepôt", href='/myview/entrepot/john', category='Espace utilisateur')
appbuilder.add_link("Commandes", href='/myview/commande/john', category='Espace utilisateur')
appbuilder.add_link("Créer un compte", href='/myview/creercompte/john', category='Espace utilisateur')
appbuilder.add_link("Commandes Fournisseurs", href='/myview/commF/john', category='Espace utilisateur')
appbuilder.add_link("Modifier le mot de passe", href='/myview/method1000/john', category='Espace utilisateur')
appbuilder.add_link("Gestion des mots de passe Client", href='/myview/ChangerMDPclient/john', category='Espace utilisateur')
appbuilder.add_link("Optimisation des trajets", href='/myview/OptimisationTrajet/john', category='Espace utilisateur')

########################          ESPACE CLIENT          ############################
appbuilder.add_link("Première connexion", href='/myview/firstconnuser/john', category='Espace Client')
appbuilder.add_link("Suivi des expéditions", href='/myview/suiviexped/john', category='Espace Client')
appbuilder.add_link("Modifier le mot de passe", href='/myview/method1000/john', category='Espace Client')
appbuilder.add_link("Historique des expéditions", href='/myview/histexped/john', category='Espace Client')




# Run the development server
app.run(debug=True)
