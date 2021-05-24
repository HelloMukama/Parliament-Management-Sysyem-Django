import sys
sys.path.append('..')  # Adding a higher directory to python modules path.
import accounts
from accounts.utils import random_code_generator

import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify   # very important for using site/username.xxx
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from .utils import unique_slug_generator
from .validators import validate_phone_number


class Meta:
    app_label = 'profiles'


# CUSTOMISING THE BUILT-IN USER MODEL to fit future needs
class MyUser(AbstractUser):  # can be referenced at 'settings.AUTH_USER_MODEL'
    """ The Profile model is gonna inherit from this 
    model now with its new customised features. """
    middle_name = models.CharField(_('middle name'), max_length=150, blank=True, null=True)
    # given_name = models.CharField(_('given name'), max_length=150, blank=True, null=True)


def user_dp_path(instance, filename):
    # saving the files to say: '/media/profilepics/user-1/abc.jpg'
    return u'profilepics/user-{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    default_dp_path = 'profilepics/default.jpg'
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    region = [('Northern', 'Northern'),
              ('Eastern', 'Eastern'),
              ('Southern', 'Southern'),
              ('Central', 'Central'),
              ('Western', 'Western')]  # option2 is what you read. option1 is whats reflected in the database
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,  related_name='profile', on_delete=models.CASCADE) # user.profile
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    # is_male = models.BooleanField(default=True)
    # is_female = models.BooleanField(default=True)
    is_mp = models.BooleanField(default=True)
    is_thespeaker = models.BooleanField(default=False)
    bio = models.TextField("About me", max_length=200, blank=True, null=True, default="Long live Uganda!")
    dp = models.ImageField(default=default_dp_path, blank=True, null=True, upload_to=user_dp_path)
    region_name = models.CharField(max_length=20, choices=region, blank=True)
    district = models.CharField(max_length=25, blank=True)
    my_constituency = models.CharField(max_length=29, blank=False)
    # phone_number = models.CharField(validators=[validate_phone_number], max_length=10, blank=False, null=False)
    phone_number = PhoneNumberField(null=True, blank=False, unique=True)
    # phone_number = PhoneNumberField(default="UG")
    slug = models.SlugField(max_length=250, null=True, blank=True)
    email = models.EmailField(verbose_name="Email address", null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username  # what will be displayed back to you on the front-end

    # fn() below is handling the saving of our profile's slug field
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    @property
    def image_url(self):
        if self.dp and hasattr(self.dp, 'url'):
            return self.dp.url

    # this method must be defined for appropriate url mapping in comments section
    def get_absolute_url(self):
        return reverse('profiles:show_self_details', kwargs={'slug': self.slug})


@receiver(post_save, sender=MyUser)
def create_related_profile(sender, instance, created, *args, **kwargs):
    """ this fn() will auto create a Profile every time a new User is created/saved.
    The profile will of course be of the same details as those provided at User creation
    This means that all we need to do is create a User and then the Profile model above will get
    auto created
    Note that we are also using 'post_save' since this fn() is called AFTER SAVING a new user
    The 'created' argument is a builtin and is a boolean. True if a new record was created.

    Notice below that we're checking for 'created'. We only want to do this
    the first time the 'User' instance is created. If the save that caused
    this signal to be run was an update action, we know the user already
    has a profile."""

    if instance and created:
        instance.profile = Profile.objects.create(user=instance)  # CREATE THE PROFILE
        # print("***********************************************")
        # if instance.profile:
        #     print(".............", instance.profile, "....................")


post_save.connect(create_related_profile, sender=MyUser)
