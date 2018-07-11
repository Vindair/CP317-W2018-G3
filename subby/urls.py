from django.urls import path

from .views import application
from .views import user

urlpatterns = [
    path('', application.index, name='index'),
    path('users', user.index, name='users_index'),
    path('users', user.index, name='users_index'),
]
