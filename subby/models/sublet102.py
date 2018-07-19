from django.db import models
from django.conf import settings
from django import forms



######################
##Temporary sublet model for report prototype purpose
######################

class Sublet102(models.Model):

    origin_input = models.CharField(max_length=250)
    destination_input = models.CharField(max_length=250)
    mode_selector = models.CharField(max_length=250)
