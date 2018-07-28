from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from subby.models import User
from django.contrib import auth
from django.contrib import messages
from django.db.models import Q
from django.db import IntegrityError

from django.contrib.auth import get_user_model

User = get_user_model()

import datetime, pytz


def __ensure_admin(func):
    def wrapper(req, *args, **kwargs):
        if req.user.is_admin != True:
            messages.error(req, 'You are not authorized to access that page')
            return redirect('subby:index')
        else:

            return func(req, *args, **kwargs)

    return wrapper


# GET /users
@__ensure_admin
def index(req):

    query = req.GET.get('query', None)

    if query == None:
        users = User.objects.filter(is_admin=False)
    else:
        users = User.objects.filter(Q(is_admin=False) & (
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query)
        )
                                    )

    return render(req, 'users/index.html', {'users': users, 'query': query})


# GET /users/:user_id
@__ensure_admin
def show(req, user_id):
    context = {'user': get_object_or_404(User, pk=user_id)}
    return render(req, 'users/show.html', context)


def contact_user(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['email'] and request.POST['message']:
            user = User.objects.get(id=request.POST['posterid'])
            user.email_user(request.POST['name'] + 'for ' + request.POST['sublettitle'], request.POST['message'],
                            request.POST['email'])
            # return render(request, 'sublet/sublet_detail.html', {'success' : 'Thanks for leaving a message! You will be contacted shortly.'})
            messages.add_message(request, messages.INFO, 'Hello world.')
            return redirect('subby:SubletDetail', request.POST['subid'])
        else:
            return render(request, 'sublet/sublet_detail.html',
                          {'error': 'All fields must be filled out when leaving contact info.'})
    else:
        return render(request, 'sublet/sublet_detail.html')


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password'] == request.POST['password-confirm']:
            try:
                user = User.objects.get(email=request.POST['username'])
                return render(request, 'application/base.html', {'signup_error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], \
                                                password=request.POST['password'])
                auth.login(request, user)
                return redirect('subby:index')
        else:
            return render(request, 'application/base.html', {'signup_error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'application/base.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            returned_render = redirect('subby:index')
        else:
            returned_render = render(request, 'application/base.html',
                                     {'login_error': 'Invalid Email or Password Entered.'})
    else:
        returned_render = render(request, 'application/base.html')

    return returned_render


# POST /logout
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('subby:index')


@__ensure_admin
def edit(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        try:
            user.email = request.POST['email']
        except Exception:
            messages.error(request, 'failed')
        else:
            user.first_name = request.POST['first']
            user.last_name = request.POST['last']
            user.phone_number = request.POST['phone']
            user.updated_at = pytz.utc.localize(datetime.datetime.now())
            user.save()
            messages.success(request, "Update Successfully")
        finally:
            return redirect('subby:user_show', user_id)
    else:
        # User wants to enter info
        return render(request, 'application/base.html')
