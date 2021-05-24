import sys
sys.path.append('..')  # Adding a higher directory to python modules path.
import profiles
# import comment
from profiles.models import Profile
# from comment.models import Comment

from django.db import models
from django.urls import reverse

from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
# from taggit.managers import TaggableManager


from .validators import validate_submission, validate_description

from django.conf import settings as project_settings
User = project_settings.AUTH_USER_MODEL


class Submission(models.Model):
    """
    Blank is different from null. null is purely database-related,
    whereas blank is validation-related(required in form).
    If null=True , Django will store empty values as NULL in the database .
    If a field has blank=True , form validation will allow entry of an empty 
    value
    """
    submission_status = (("solved", "Solved"),
                         ("inprogress", "In Progress"),
                         ("pending", "Pending"))

    submission_cat = (("Agriculture", "Agriculture"),
                      ("Education", "Education"),
                      ("Health", "Health"),
                      ("Industry", "Industry"),
                      ("Security", "Security"),
                      ("Technology", "Technology"),
                      ("Tourism", "Tourism"),
                      ("Others", "Others"))

    regions_list = (("Central", "Central Uganda"),
                    ("Southern", "Southern Uganda"),
                    ("Eastern", "Eastern Uganda"),
                    ("Northern", "Northern Uganda"),
                    ("Western", "Western Uganda"))

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    region = models.CharField(max_length=200, choices=regions_list, blank=False, null=False)
    district = models.CharField(max_length=200, blank=False, null=False)
    constituency = models.CharField(max_length=200, blank=False, null=False)
    submission = models.CharField(max_length=60, blank=False, null=False, validators=[validate_submission])
    submission_category = models.CharField(choices=submission_cat, blank=False, null=False, max_length=200)
    description = models.TextField(max_length=500, blank=False, null=False, validators=[validate_description])
    comments = GenericRelation(Comment)
    submission_status = models.CharField(max_length=200, choices=submission_status, null=True, blank=True, default="pending")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # tags = TaggableManager()

    class Meta:
        ordering = ("-timestamp", )

    def __str__(self):
        return self.submission

    def get_absolute_url(self):
        return reverse('submissions:submission_detail', kwargs={'pk': self.pk})
