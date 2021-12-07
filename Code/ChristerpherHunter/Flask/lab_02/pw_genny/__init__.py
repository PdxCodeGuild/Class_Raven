from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config["SECRET_KEY"] = "12$KMB0IMz2qMrQ0l4.o66Sxuz11KPc5FY4eXmJ6HabOoweuA2ehH172"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

from pw_genny import routes