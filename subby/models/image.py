from django.db import models
from django.conf import settings
from subby.models.sublet import Sublet

class Image(models.Model):
    sublet = models.ForeignKey(Sublet, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)