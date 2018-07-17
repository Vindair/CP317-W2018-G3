from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from subby.models.sublet import Sublet
from django.utils import timezone
from django.contrib.auth.models import User


def account_home(request):
	
	return render(request, 'users/account_home.html')


