from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse("User index route")

def show(req, user_id):
    res = "Show user %s"
    return HttpResponse(respons % id)
