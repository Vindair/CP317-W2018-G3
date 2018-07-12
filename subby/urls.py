from django.urls import path

from .views import application
from .views import user

urlpatterns = [
    path('', application.index, name='index'),
    path('users', user.index, name='user_index'),
    path('users/<int:user_id>', user.show, name='user_show'),
]
