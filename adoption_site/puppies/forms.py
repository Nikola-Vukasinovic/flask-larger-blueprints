from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField("Name of Pup:")
    submit = SubmitField("Add puppy")


class DelForm(FlaskForm):
    id = IntegerField("Id Number of puppy to delete")
    submit = SubmitField("Delete puppy")