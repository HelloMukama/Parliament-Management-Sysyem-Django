from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django import forms

from django.conf import settings
User = settings.AUTH_USER_MODEL


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)
