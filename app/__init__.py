from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')

from app import routes

# Create the Parrott!
from parrott import Parrott
app.parrott = Parrott()

# This works!
tweet_id='544eea61-a583-4ec9-af50-7c40ff47671f'
# Fetch current tweet
tweet = app.parrott.memory.recall(tweet_id)
# If a matching tweet was found, audit as positive
if tweet:
    app.parrott.audit(tweet, True) # test auditing
