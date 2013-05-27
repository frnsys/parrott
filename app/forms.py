# Form & Fields
from flask.ext.wtf import Form, TextField, BooleanField

# Validators
from flask.ext.wtf import Required

class ClassifyForm(Form):
    tweet = TextField('tweet', validators=[Required()])
