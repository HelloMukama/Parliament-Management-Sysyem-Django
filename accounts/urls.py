from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.urls import re_path
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView


app_name = 'accounts'

urlpatterns = [
    # account/

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password-change/', login_required(auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html', success_url=reverse_lazy('accounts:logout'))), name='password_change'),

    # class  PasswordChangeView has an builtin login_required as seen in the class dispatch below
    # All CBV do
    # So there is really no need of adding the decorator again as above but lets leave it for now..
    # @method_decorator(sensitive_post_parameters())
    # @method_decorator(csrf_protect)
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', email_template_name='accounts/password_reset_email.html', subject_template_name='accounts/password_reset_subject.txt', success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset_<uidb64>_<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')), name='password-reset-confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
