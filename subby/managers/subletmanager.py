from django.db import models
from django.conf import settings

class SubletManager(models.Manager):
	def get_cover_image(self):
		qs = self.get_queryset()
		print(qs)
		return qs