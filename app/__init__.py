from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from app import routes

# Create the Parrott!
from parrott import Parrott
app.parrott = Parrott()

tweet_id = 'b7aac0e9-5f3f-4a56-abc2-6653ba961d5b'
tweet = app.parrott.memory.recall(tweet_id) # check if this returns a list or a single object
import pdb; pdb.set_trace()
