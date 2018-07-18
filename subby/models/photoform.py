from subby.models.photo import Photo
from django.forms import ModelForm

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )