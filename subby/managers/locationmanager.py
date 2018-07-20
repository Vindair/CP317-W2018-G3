from django.db import models
from django.conf import settings
from django.db.models.expressions import RawSQL

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