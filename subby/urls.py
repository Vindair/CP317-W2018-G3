from django.urls import path

from .views import application, user

app_name = 'subby'

urlpatterns = [
    # Base application view (i.e. index, about, contact...)
    path('', application.index, name='index'),

    # User views
    path('users', user.index, name='user_index'),
    path('users/<int:user_id>', user.show, name='user_show')
]
