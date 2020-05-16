from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired

class UploadForm(FlaskForm):
    description = StringField('description',widget=TextArea(), validators=[InputRequired()])
    photo = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])