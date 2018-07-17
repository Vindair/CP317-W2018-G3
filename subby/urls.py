from django.urls import path

from .views import application, user, sublet, account
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
	##Temporary login/signup/logout path for report prototype
	################
	path('login/', user.login, name='login'),
	path('logout/', user.logout, name='logout'),
	path('signup/', user.signup, name='signup'),
	
	
	################
	##Temporary sublet path for report prototype
	################
	path('sublets/', sublet.SubletList.as_view(template_name='sublet/sublet_list.html'), name='SubletList'),
	
	path('sublets/<int:pk>/', sublet.SubletDetail.as_view(template_name='sublet/sublet_detail.html'), name='SubletDetail'),
	
	path('sublets/create_sublet', sublet.create_sublet, name='create_sublet'),
	
	##############
	##Temporary account path for report prototype
	##############
	path('account/', account.account_home, name='account_home'),
	
	
	
	
]

