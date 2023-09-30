from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf, URL

class AddPetForm(FlaskForm):
    """ Form to add pet. """
    name = StringField('Name',
    validators = [
        InputRequired()
    ])

    species = StringField('Species',
    validators = [
        InputRequired(),
        AnyOf(values=['dog', 'cat', 'porcupine'], message='Only dog, cat, and porcupine are accepted')
    ])

    photo_url = StringField('Photo',
    validators = [
        Optional(),
        URL(message='Must be a valid url')
    ])

    age = IntegerField('Age', 
    validators=[
        Optional(),
        NumberRange(min=0, max=30, message='Age must be from 0 to 100')
    ])

    notes = TextAreaField('Notes',
    validators = [
        Optional()
    ])

class UpdatePetForm(FlaskForm):
    """ Form to update pet. """
    photo_url = StringField('Photo',
    validators = [
        Optional(),
        URL(message='Must be a valid url')
    ])
    
    notes = TextAreaField('Notes',
    validators = [
        Optional()
    ])

    available = BooleanField('Available')