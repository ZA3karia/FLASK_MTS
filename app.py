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

    default_view = 'M_optimiser'

    
    @expose('/M_optimiser/<string:param1>')
    @has_access
    def M_optimiser(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'the optimal route is %s' % (param1)
        self.update_redirect()
        return self.render_template('method_optimiser.html',
                            param1 = param1)

appbuilder.add_view(MyView, "M_optimiser", href='/myview/M_optimiser/test', category='My View')
#appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
#appbuilder.add_link("Method3", href='/myview/method3/mark', category='My View')
# Run the development server
app.run(debug=True)

