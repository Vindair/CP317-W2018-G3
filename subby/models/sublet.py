from django.db import models




######################
##Temporary sublet model for report prototype purpose
######################

class Sublet(models.Model):
	
	title = models.CharField(max_length=50)
	street_address = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=7)
	city = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now=True)
	price = models.FloatField()
	description = models.TextField()
	front_image = models.ImageField(upload_to='images/', default='subby_project/images/example.jpg')
	
	def summary(self):
		return self.description[:180]
		