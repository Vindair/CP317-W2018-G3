from django.db import models
from django.conf import settings
from django import forms



######################
##Temporary sublet model for report prototype purpose
######################

class Sublet101(models.Model):
	SET_OF_CHOICES = (
	('W', 'Walking'),
	('T', 'Transit'),
	('D', 'Walking'),

	)
    # origin_input = models.CharField(max_length=250)
    # destination_input = models.CharField(max_length=250)
    # mode_selector = models.CharField(max_length=250)
	origin_input = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(blank=True, null=True)
	choice = models.CharField(max_length=250, choices=SET_OF_CHOICES)
	latitude = models.FloatField()
	longitude = models.FloatField()
	title = models.CharField(max_length=50)
	price = models.FloatField()
	postal_code = models.CharField(max_length=7)
	city = models.CharField(max_length=20)
	street_address = models.CharField(max_length=250)
