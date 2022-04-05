from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.fields import FileField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class DocumentUploadForm(FlaskForm):
    """DocumentUploadForm Object meant to create the form for submitting Whole Slide Image Data

    The form has 4 fields which are the EmailField, the FileField, the ModelField, and the SubmitField. 
        The EmailField will have the pathologist set their email, so that when the image classification is done,
            they will be notified by email.
        The FileField will have the pathologist choose which of the Whole Slide Image files that they want to
            upload to the ML model.
        The ModelField will have the pathologist choose the model that they will use to analyze the new image.
        The SubmitField will be the button that submits the form the server for processing.
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    file = FileField('Images', validators=[FileRequired(), FileAllowed(['tiff', 'svs', 'jpg', 'jpeg'], 'Whole Slide Image Data Only!')])
    model = StringField('Model', validators=[DataRequired()])
    submit = SubmitField('Submit Images')
