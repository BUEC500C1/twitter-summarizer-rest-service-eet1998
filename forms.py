from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HandleForm(FlaskForm):
    handle = StringField('Handle', validators=[DataRequired()])
    get_video = SubmitField('Get video!')
