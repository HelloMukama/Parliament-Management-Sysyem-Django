from django.urls import path

from .views import PersonalSettingsTemplateView

app_name = "personalsettings"

urlpatterns = [
    # settings/system/...
    path('', PersonalSettingsTemplateView.as_view(), name="personalsettings"),
]
