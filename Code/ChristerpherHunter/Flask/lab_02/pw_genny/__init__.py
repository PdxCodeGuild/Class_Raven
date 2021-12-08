
from flask import Flask


app = Flask(__name__)

app.config["SECRET_KEY"] = "12$KMB0IMz2qMrQ0l4.o66Sxuz11KPc5FY4eXmJ6HabOoweuA2ehH172"

from pw_genny import routes