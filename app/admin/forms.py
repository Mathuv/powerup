# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class WorkItemForm(FlaskForm):
    """
    Form for admin to add or edit a Work Item
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
