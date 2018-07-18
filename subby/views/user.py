from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from subby.models import User
from django.contrib import auth

from django.contrib.auth.models import User as Users

def index(req):
    context = { 'users': get_list_or_404(User) }
    return render(req, 'users/index.html', context)

def show(req, user_id):
    context = { 'user': get_object_or_404(User, pk = user_id) }
    return render(req, 'users/show.html', context)



####################################
##Temporary user views (default
##Authentication and Authorization used)
##for report prototype purpose
##including signup, login, logout. 
####################################

def signup(request):
	if request.method == 'POST':
		#User has info and wants an account now!
		if request.POST['password'] == request.POST['password-confirm']:
			try: 
				user = Users.objects.get(username = request.POST['username'])
				return render(request, 'application/base.html', {'error':'Username has already been taken'})
			except Users.DoesNotExist:
				user = Users.objects.create_user(request.POST['username'], \
				password = request.POST['password'])
				auth.login(request, user)
				return redirect('subby:index')
		else:
			return render(request, 'application/base.html', {'error':'passwords must match'})
	else:
		#User wants to enter info
		return render(request, 'application/base.html')
		
		
def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			returned_render = redirect('subby:index')
		else:
			returned_render = render(request, 'application/base.html',{'login_error':'Invalid Email or Password Entered.'})
	else:
		returned_render = render(request, 'application/base.html')
	
	return returned_render
	
def logout(request):

	if request.method == 'POST':
		auth.logout(request)
		return redirect('subby:index')
		

