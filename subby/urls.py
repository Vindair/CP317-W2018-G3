from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import application, user, sublet, account


app_name = 'subby'

urlpatterns = [
  # Base application view
  path('', application.index, name='index'),

  # User Admin views
  path('users/', user.index, name='user_index'),
  path('users/<int:user_id>', user.show, name='user_show'),

  # User session views
  path('login/', user.login, name='login'),
  path('logout/', user.logout, name='logout'),
  path('signup/', user.signup, name='signup'),

  # Account Paths
  path('account/', account.account_home, name='account_home'),
  path('account/update', account.update_user_info, name='update_user_info'),

  # Sublet paths
  path('sublets/', sublet.SubletList.as_view(template_name='sublet/sublet_list.html'), name='SubletList'),
  path('sublets/<int:pk>/', sublet.SubletDetail.as_view(template_name='sublet/sublet_detail.html'), name='SubletDetail'),
  path('sublets/create_sublet', sublet.create_sublet, name='create_sublet'),
  path('sublets/search', sublet.search, name='search'),
  path('sublets/contact', user.contact_user, name='contact_user'),
]
