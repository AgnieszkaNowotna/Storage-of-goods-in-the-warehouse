from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired

choices = ['kg','pcs','l']

class ProductForm(FlaskForm):
    name = StringField('name', validators = [DataRequired()])
    quantity = IntegerField('quantity', validators = [DataRequired()])
    unit = SelectField('unit', choices = choices, coerce = str, validators = [DataRequired()])
    unit_price = FloatField('unit_price', validators = [DataRequired()])