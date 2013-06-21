from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')

from app import routes

# Create the Parrott!
from parrott import Parrott
app.parrott = Parrott()
