import os
from flask import Flask, render_template
from flask_appbuilder import SQLA, AppBuilder, AppBuilder, expose, BaseView, has_access
# init Flask
app = Flask(__name__)
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
    default_view = 'AccueilAdmin'
    @expose('/AccueilAdmin/')
    @has_access
    def AccueilAdmin(self):
        # do something with param1
        # and return to previous page or index
        return 'Hello'



    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1


    @expose('/Fonctionnalités/<string:param1>')
    @has_access
    def method3(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('methode3.html',
                            param1 = param1)


appbuilder.add_view(MyView, "Accueil Admin", category='Espace Admin')
appbuilder.add_link("Method2", href='/myview/method2/john', category='Espace Admin')
appbuilder.add_link("Fonctionnalités", href='/myview/Fonctionnalités/john', category='Espace Admin')



appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
appbuilder.add_link("Methode3", href='/myview/methode3/john', category='My View')



        



# Run the development server
app.run(debug=True)
