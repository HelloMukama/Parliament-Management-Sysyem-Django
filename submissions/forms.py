from django import forms
import django_filters

from .models import Submission  # , Comment


class SubmissionCreateForm(forms.ModelForm):
    
    # https://stackoverflow.com/questions/41271979/read-only-field-in-django-form     <<--- FINALLY
    region = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), label='Region of Interest')
    district = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), label='District of Interest')
    constituency = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), label='Constituency of Interest')

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Details can not exceed 500 characters',
    }), label='Details of submission')

    class Meta:
        model = Submission
        fields = [
            'submission',
            'region',
            'district',
            'constituency',
            'submission_category',
            'description'
        ]


class SubmissionStatusSpeakerUpdateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('submission_status',)
        
        CHOICES = [("solved", "Solved"),
                   ("inprogress", "In Progress"),
                   ("pending", "Pending")
                   ]
        submission_status = forms.CharField(label='S-Status', widget=forms.RadioSelect(choices=CHOICES))


class SubmissionUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }), label='Edit submission details here')

    class Meta:
        model = Submission
        fields = ('submission', 'submission_category', 'description')


class SubmissionFilter(django_filters.FilterSet):
    class Meta:
        model = Submission
        fields = ['district', 'region', 'submission', 'submission_category']
