from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from app import routes

# Create the Parrott!
import parrott
parrott = Parrott()
