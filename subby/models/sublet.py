from django.db import models
from django.conf import settings



######################
##Temporary sublet model for report prototype purpose
######################

class Sublet(models.Model):


	street_address = models.CharField(max_length=250)
	latitude = models.FloatField()
	longitude = models.FloatField()
	postal_code = models.CharField(max_length=7)
	city = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(blank=True, null=True)
	description = models.TextField()
	title = models.CharField(max_length=50)
	price = models.FloatField()

	front_image = models.ImageField(upload_to='images/', null=True, blank=True)

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def summary(self):
		if len(self.description) > 150:
			return self.description[:150] + "......"
		else:
			return self.description
