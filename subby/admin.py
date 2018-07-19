from django.contrib import admin
from .models import *
from .models.sublet import Sublet
admin.site.register(User)
from .models.sublet102 import Sublet102



class SubletData(admin.ModelAdmin):
	list_display = ('title', 'street_address', 'created_at', 'updated_at')
admin.site.register(Sublet, SubletData)
admin.site.register(Sublet102)
