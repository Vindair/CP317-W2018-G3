from django.urls import path

from .views import application, user
from django.conf.urls.static import static
from django.conf import settings

app_name = 'subby'

urlpatterns = [
    # Base application view (i.e. index, about, contact...)
    path('', application.index, name='index'),

    # User views
    path('users/', user.index, name='user_index'),
    path('users/<int:user_id>', user.show, name='user_show'),
	
	
	################
	##Temporary path for report prototype
	################
	path('login/', user.login, name='login'),
	path('logout/', user.logout, name='logout'),
	path('signup/', user.signup, name='signup'),
	
]

