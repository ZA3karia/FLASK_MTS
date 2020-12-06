import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__,static_url_path = "/static", static_folder = "static")
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

from . import models, views  # noqa