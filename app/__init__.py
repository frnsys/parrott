from flask import Flask
app = Flask(__name__)
from app import routes, models

# Create the Parrott!
import parrott
parrott = Parrott()
