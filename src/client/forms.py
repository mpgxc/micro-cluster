
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class Entrada(Form):

    Palavras1 = StringField('Palavras1', validators = [DataRequired(), validators.Length(min=4, max=25)])
    Palavras2 = StringField('Palavras2', validators = [DataRequired(), validators.Length(min=4, max=25)])
    Palavras3 = StringField('Palavras3', validators = [DataRequired(), validators.Length(min=4, max=25)])
    Texto = TextAreaField("Texto", validators = [DataRequired(),validators.Length(min=4, max=255)])
