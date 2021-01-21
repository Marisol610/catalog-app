#!/products/bin/env python3
#-*- coding utf8 -*-
""" This is the app product definition"""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField("What is the product's name?", validators=[DataRequired()])
    price = StringField("How much will it cost?", validators=[DataRequired()])
    description = StringField("Enter a description", validators=[DataRequired()])
    category = StringField("What's the product's category?", validators=[DataRequired()])
    quantity = StringField("Enter a description", validators=[DataRequired()])
    unique_tag = StringField("What's the product's category?", validators=[DataRequired()])
    submit = SubmitField("Submit")