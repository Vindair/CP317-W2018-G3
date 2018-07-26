from django.urls import path

from .views import application, user, sublet, account, rating
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

	path('sublets/update_sublet', sublet.update_sublet, name='update_sublet'),

	path('sublets/search', sublet.search, name='search'),

	path('sublets/contact', user.contact_user, name='contact_user'),
	
	##############
	##Temporary account path for report prototype
	##############
	path('account/', account.account_home, name='account_home'),
	path('account/update', account.update_user_info, name='update_user_info'),
	

	path('ratings/<int:user_id>', rating.list_user_rating, name='RatingList'),

	path('ratings/write_review/', rating.write_review, name='write_review'),
	path('ratings/update_review/', rating.update_review, name='update_review'),
	path('ratings/reviews/<int:pk>/', rating.my_review, name='my_review'),
	path('ratings/delete/<int:rating_id>/<int:reviewed_user_id>/', rating.delete_review, name='delete_review'),

]

