from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import PermissionsMixin

from phonenumber_field.formfields import PhoneNumberField

from .models import MyUser, Profile


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text=None)
    first_name = forms.CharField(max_length=20, help_text=None, required=False)
    last_name = forms.CharField(max_length=20, help_text=None, required=False)

    class Meta:
        model = MyUser
        # fields = ('username', 'first_name', 'last_name', )
        # fields = UserCreationForm.Meta.fields + ('middle_name', )
        fields = ("__all__")


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', )


class EditProfileForm(forms.ModelForm):
    phone_number = PhoneNumberField()
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Self description can not exceed 200 characters',
        'rows': 4,
    }), label='About you')

    # https://stackoverflow.com/questions/14336925/how-to-not-render-django-image-field-currently-and-clear-stuff
    dp = forms.ImageField(label='Your photo' ,required=False, error_messages = {'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = (
            # 'user',     # we want to make sure the user cannot change their username.
            'email',
            'phone_number',
            'bio',
            'dp'
        )
