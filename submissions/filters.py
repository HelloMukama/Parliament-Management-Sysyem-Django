import django_filters
from django_filters import DateFilter, CharFilter
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# from bootstrap_datepicker_plus import DatePickerInput


from .models import *


class TableFilter(django_filters.FilterSet):
    """ NB: 'icontains' means ignore case. 'i' for 'ignore'
    """
    STATUS_CHOICES = (
        ("solved", "Solved"), 
        ("inprogress", "In Progress"), 
        ("pending", "Pending")
        )
    submission_cat = (("Agriculture", "Agriculture"),
        ("Education", "Education"),
        ("Health", "Health"), 
        ("Industry", "Industry"), 
        ("Security", "Security"),
        ("Technology", "Technology"),
        ("Tourism", "Tourism"),
        ("Others", "Others")
        )
    regions_list = (
        ("Central", "Central Uganda"),
        ("Southern", "Southern Uganda"),
        ("Eastern", "Eastern Uganda"),
        ("Northern", "Northern Uganda"),
        ("Western", "Western Uganda")
        )
    submission = CharFilter(field_name='submission', lookup_expr='icontains')
    submission_category = django_filters.ChoiceFilter(choices=submission_cat, field_name='submission_category', lookup_expr='icontains')
    region = django_filters.ChoiceFilter(choices=regions_list, field_name='region', lookup_expr='icontains')
    district = CharFilter(field_name='district', lookup_expr='icontains')
    submission_status = django_filters.ChoiceFilter(choices=STATUS_CHOICES, field_name='submission_status', lookup_expr='icontains')
    start_date = DateFilter(field_name="timestamp", lookup_expr='gte')
    end_date = DateFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Submission
        fields = '__all__'
        exclude = ['profile', 'description', 'constituency', 'date_created', 'timestamp', 'updated']
        # widgets = {
        #     'start_date': DatePickerInput(format='%d-%m-%Y'), # default date-format %m/%d/%Y will be used
        #     'end_date': DatePickerInput(format='%d-%m-%Y'), # specify date-frmat
        # }
