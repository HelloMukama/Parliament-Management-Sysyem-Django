import sys
sys.path.append('..')  # Adding a higher directory to python modules path.
import profiles
from profiles.models import Profile

# from django.contrib.auth import get_user_model
from django.contrib import admin

from django.conf import settings as project_settings
User = project_settings.AUTH_USER_MODEL

from .models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('submission',
                    'profile',
                    'district',
                    'region',
                    # 'description',
                    'submission_category',
                    'submission_status',
                    'timestamp',
                    )
    ordering = ['timestamp', ]


admin.site.register(Submission, SubmissionAdmin)
