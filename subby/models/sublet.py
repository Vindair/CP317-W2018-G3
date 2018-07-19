from django.db import models
from django.conf import settings
from django.db.models.expressions import RawSQL


######################
##Temporary sublet model for report prototype purpose
######################
class LocationManager(models.Manager):
    def nearby(self, latitude, longitude, proximity):
        """
        Return all object which distance to specified coordinates
        is less than proximity given in kilometers
        """
        # Great circle distance formula
        gcd = """
              6371 * acos(
               cos(radians(%s)) * cos(radians(latitude))
               * cos(radians(longitude) - radians(%s)) +
               sin(radians(%s)) * sin(radians(latitude))
              )
              """
        return self.get_queryset()\
                   .exclude(latitude=None)\
                   .exclude(longitude=None)\
                   .annotate(distance=RawSQL(gcd, (latitude,
                                                   longitude,
                                                   latitude)))\
                   .filter(distance__lt=proximity)\
                   .order_by('distance')

class SubletManager(models.Manager):
	def get_cover_image(self):
		qs = self.get_queryset()
		print(qs)
		return qs

class Sublet(models.Model):
	objects = LocationManager()
	latitude = models.FloatField()
	longitude = models.FloatField()

	street_address = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=7)
	city = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(blank=True, null=True)
	description = models.TextField()
	title = models.CharField(max_length=50)
	price = models.FloatField()

	images = SubletManager()
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def summary(self):
		if len(self.description) > 150:
			return self.description[:150] + "......"
		else:
			return self.description

class SubletImage(models.Model):
	sublet = models.ForeignKey(Sublet, related_name='sublet', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='image/')


		