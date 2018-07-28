from functools import wraps
from django.utils.decorators import available_attrs
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required

default_message = "Please login to view the requested page."
default_login = "/login/"


def user_passes_test(test_func, message=default_message):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                messages.error(request, message)
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


def login_required_message(function=None, message=default_message):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        message=message,
    )
    if function:
        return actual_decorator(function)

def message_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=default_login, message=default_message):

    if function:
        return login_required_message(
            login_required(function, redirect_field_name, login_url),
            message
        )

    return lambda deferred_function: message_login_required(deferred_function, redirect_field_name, login_url, message)
