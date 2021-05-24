from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PersonalSettingsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "personalsettings/personalsettings.html"
