from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from subby.models import User
from django.contrib import auth
from django.contrib import messages

#from django.contrib.auth.models import User as Users

from django.contrib.auth import get_user_model
User = get_user_model()

def index(req):
    context = { 'users': get_list_or_404(User) }
    return render(req, 'users/index.html', context)

def show(req, user_id):
    context = { 'user': get_object_or_404(User, pk = user_id) }
    return render(req, 'users/show.html', context)


def contact_user(request):
	if request.method == 'POST':
		if request.POST['name'] and request.POST['email'] and request.POST['message']:
			user = User.objects.get(id = request.POST['posterid'])
			user.email_user(request.POST['name'] + 'for ' + request.POST['sublettitle'], request.POST['message'], request.POST['email'])
			#return render(request, 'sublet/sublet_detail.html', {'success' : 'Thanks for leaving a message! You will be contacted shortly.'})
			messages.add_message(request, messages.INFO, 'Hello world.')
			return redirect('subby:SubletDetail', request.POST['subid'])
		else:
			return render(request, 'sublet/sublet_detail.html', {'error' : 'All fields must be filled out when leaving contact info.'})
	else:
		return render(request, 'sublet/sublet_detail.html')


def signup(request):
	if request.method == 'POST':
		#User has info and wants an account now!
		if not request.POST['username']:
			return render(request, 'application/base.html', {'signup_error' : 'Please enter an email address'})
		if request.POST['password'] == request.POST['password-confirm']:
			try: 
				user = User.objects.get(email = request.POST['username'])
				return render(request, 'application/base.html', {'signup_error':'Username has already been taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], \
				password = request.POST['password'])
				auth.login(request, user)
				return redirect('subby:index')
		else:
			return render(request, 'application/base.html', {'signup_error':'Passwords must match'})
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
		

