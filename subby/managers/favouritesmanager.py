from django.db import models
from django.conf import settings
import datetime, pytz

class FavouriteManager(models.Manager):

    def create_favourite(self, sublet, user):
        favourite = self.model()
        favourite.sublet = sublet
        favourite.user = user
        favourite.save()
        return favourite