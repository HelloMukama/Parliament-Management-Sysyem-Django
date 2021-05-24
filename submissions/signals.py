import sys
sys.path.append('..')  # Adding a higher directory to python modules path.

import complaints, accounts, profiles
from complaints.models import MySubmission
from profiles.models import Profile

# NB:: THE lines above are for the BLOODY relative import

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()


# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#
#     if created:
#         complaint = Complaint(user=user)
#         complaint.save()
