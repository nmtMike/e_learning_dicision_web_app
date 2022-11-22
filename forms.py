from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Check_Form(FlaskForm):

    provider = StringField('Provider Name: ')
    approach = StringField('Approach: ')
    material = StringField('Material: ')
    submit = SubmitField('Check')
