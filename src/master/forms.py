# -*- coding: utf-8 -*-
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class Entrada(Form):

    name = StringField("nome", validators = [DataRequired(),validators.Length(min=4, max=25)])
    
    ip = StringField("ip", validators = [DataRequired(),validators.Length(min=4, max=25)])
    
    ram = StringField("ram", validators = [DataRequired(),validators.Length(min=4, max=25)])

    cores = StringField("cores", validators = [DataRequired(),validators.Length(min=4, max=25)])
    