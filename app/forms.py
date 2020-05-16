from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from wtforms import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired

images = UploadSet('images', IMAGES)

class UploadForm(FlaskForm):
    description = TextArea('description', validators=[InputRequired()])
    photo = FileField('image', validators=[FileRequired(),FileAllowed(images, 'Images only!')])