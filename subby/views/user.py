from django.shortcuts import render
from django.http import HttpResponse
from subby.models import User

def index(req):
    return HttpResponse("User index route")

def show(req, user_id):
    res = "Show user %s"
    user = User.objects.get(pk = user_id)
    return HttpResponse(res % user)
