import sys
sys.path.append('..')  # Adding a higher directory to python modules path.
import profiles
from profiles.models import Profile

# NB:: THE lines above are for the BLOODY relative import

from .forms import LoginForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView

from django.conf import settings
from django.views.generic import CreateView

User = settings.AUTH_USER_MODEL


# Code below, we are not using because we are going with builtin login class
# class AccountLoginView(bracesviews.AnonymousRequiredMixin, LoginView):
class AccountLoginView(LoginView):
    template_name = "accounts/signin.html"
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        stu_mem = self.request.user.profile.type_user

        if remember_me is True:
            ONE_MONTH = 30*24*60*60
            expiry = getattr(settings, "KEEP_LOGGED_DURATION", ONE_MONTH)
            self.request.session.set_expiry(expiry)

        if stu_mem == 'mp' or stu_mem == 'citizen':
            # Redirecting the basic_user to the dashboard
            return redirect('/profile/dashboard')
        elif stu_mem == 'speaker_office':
            # Redirecting the admin to the complaints list page
            return redirect(reverse('complaints:all_complaints'))
        else:
            return redirect(reverse('complaints:all_complaints'))

        # return super(AccountLoginView, self).form_valid(form)   # unindent 4 spaces
