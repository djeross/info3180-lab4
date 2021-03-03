from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired,Regexp

class UploadForm(FlaskForm):
    image= FileField(u'Upload Image File', [DataRequired()])


"""def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)"""