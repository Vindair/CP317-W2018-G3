from django.shortcuts import get_object_or_404, get_list_or_404, render
from subby.models import User

def index(req):
    context = { 'users': get_list_or_404(User) }
    return render(req, 'users/index.html', context)

def show(req, user_id):
    context = { 'user': get_object_or_404(User, pk = user_id) }
    return render(req, 'users/show.html', context)
