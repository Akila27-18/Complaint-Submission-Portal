
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ComplaintForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    message = TextAreaField('Complaint', validators=[DataRequired()])
    submit = SubmitField('Submit')
