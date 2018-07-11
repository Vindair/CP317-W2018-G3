from django.db import models

class User(models.Model):
    email = models.CharField(max_length = 200)
    first_name = models.CharField(max_length = 200, null = True)
    last_name = models.CharField(max_length = 200, null = True)
    phone_number = models.CharField(max_length = 31, null = True)
    is_admin = models.BooleanField()
    password = models.CharField(max_length = 200)
    salt = models.CharField(max_length = 20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'subby'
