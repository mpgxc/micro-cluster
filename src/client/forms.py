
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class Entrada(Form):

    Palavras = StringField('Palavras', validators = [DataRequired(), validators.Length(min=4, max=25)])
    Texto = TextAreaField("Texto", validators = [DataRequired(),validators.Length(min=4, max=255)])
