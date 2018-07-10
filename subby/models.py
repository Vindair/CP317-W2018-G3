from django.db import models

class User(models.Model):
    email = models.CharField(max_length = 200)
    is_admin = models.BooleanField()
