from django.contrib import admin
from .models import *
from .models.sublet import Sublet
admin.site.register(User)



class SubletData(admin.ModelAdmin):
	list_display = ('title', 'street_address', 'pk')
admin.site.register(Sublet, SubletData)