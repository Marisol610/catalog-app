#!/products/bin/env python3
#-*- coding utf8 -*-
""" This is the app product definition"""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired





class ProductForm(FlaskForm):
    name = StringField("Enter the product's name", validators=[DataRequired()])
    price = StringField("Enter the product' price", validators=[DataRequired()])
    description = StringField("Enter the product's description", validators=[DataRequired()])
    category = StringField("Enter the product's category", validators=[DataRequired()])
    quantity = StringField("Enter a quantity", validators=[DataRequired()])
    unique_tag = StringField("Enter the product's unique_tag", validators=[DataRequired()])
    submit = SubmitField("Submit")