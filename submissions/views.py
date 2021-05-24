import sys
sys.path.append('..')  # Adding a higher directory to python modules path.
import profiles
from profiles.models import MyUser, Profile
from mysite import settings

from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.core.mail import send_mail
from datetime import datetime
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView
# from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django import forms

from django.conf import settings as project_settings

from .filters import TableFilter
from .forms import (
                    SubmissionCreateForm, 
                    # SubmissionStatusUpdateForm, 
                    SubmissionStatusSpeakerUpdateForm,
                    SubmissionUpdateForm  # , CommentForm 
                    )
from .mixins import UserOwnerMixin, FormUserNeededMixin
from .models import Submission  #, Comment

User = project_settings.AUTH_USER_MODEL


class SubmissionCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    template_name = 'submissions/submission_create.html'
    model = Submission
    form_class = SubmissionCreateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={
            'region': request.user.profile.region_name,
            'district': request.user.profile.district,
            'constituency': request.user.profile.my_constituency
        })
        print(form['district'].value(), '********************')
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile = request.user.profile
            mail = request.user.profile.email
            # print("\n\n\n>>>>>>>>>>>>>>>>>>>>>", mail, "<<<<<<<<<<<<<<<<<<<<")
            # send_mail(subject, msg, from, to, kwargs)   # to can be a recipient list
            send_mail("Submission Received!", "Hi {}, your submission has been received at the speaker's desk. Keep checking your inbox for updates from our office as regards this very submission. Thank you. Do not Reply to this mail".format(request.user.first_name), settings.EMAIL_HOST_USER, [request.user.profile.email, ], fail_silently=False)
            print("\n\n")
            instance.save()
            # messages.add_message(request, messages.SUCCESS, f'Submission was Logged!!!')
            # messages.add_message(request, messages.SUCCESS, 'Submission was Logged!!!')
            return redirect(reverse('submissions:all_submissions'))
        else:  # return form
            form = SubmissionCreateForm(request.POST)
            context = {'form': form, }
            return render(request, self.template_name, context)
            # return redirect(reverse('submissions:unsolved_submissions'), )


class AllSubmissionsListView(LoginRequiredMixin, ListView):   # MP
    context_object_name = 'all_submissions_list'
    template_name = "submissions/all_submissions.html"
    # paginate_by = 10

    def get_queryset(self):
        # returning everything that is owned by the current user.
        qs = Submission.objects.filter(profile__user=self.request.user).order_by('timestamp')
        return qs


class UnsolvedSubmissionsListView(LoginRequiredMixin, ListView):   # MP
    context_object_name = 'unsolved_submissions_list'
    template_name = "submissions/unsolved_submissions.html"
    # paginate_by = 10

    def get_queryset(self):
        # returning whats owned by current user but not solved..
        qs = Submission.objects.filter(profile__user=self.request.user).exclude(
            Q(submission_status__icontains='solved')).order_by('-timestamp')
        return qs


class SolvedSubmissionsListView(LoginRequiredMixin, ListView):   # MP
    context_object_name = 'solved_submissions_list'
    template_name = "submissions/solved_submissions.html"
    # paginate_by = 10

    def get_queryset(self):
        # returning whats owned by current user but not solved..
        qs = Submission.objects.filter(profile__user=self.request.user).filter(
            Q(submission_status__icontains='solved')).order_by('-timestamp')
        return qs


# class TheSpeakerAllSubmissionsListView(LoginRequiredMixin, ListView):
#     context_object_name = 'thespeaker_all_submissions_list'
#     template_name = "submissions/all_submissions.html"
#     paginate_by = 10
#     model = Submission
#     filterset_class = TableFilter()

#     def get_queryset(self):
#         qs = Submission.objects.all().order_by('timestamp')
#         return qs


@login_required
def the_speaker_all_submissions_list(request):    # ALL
    submissions = Submission.objects.all()

    # orders = customer.order_set.all()
    # order_count = orders.count()

    my_filter = TableFilter(request.GET, queryset=submissions)
    submissions = my_filter.qs 

    context = {
        'thespeaker_all_submissions_list': submissions, 
        # 'orders': orders, 
        # 'order_count': order_count,
        'my_filter': my_filter
        }
    return render(request, 'submissions/all_submissions.html', context)


# class TheSpeakerUnsolvedSubmissionsListView(LoginRequiredMixin, ListView):
#     context_object_name = 'thespeaker_unsolved_submissions_list'
#     template_name = "submissions/unsolved_submissions.html"
#     # paginate_by = 10

#     def get_queryset(self):
#         # returning whats owned by current user but not solved..
        # qs = Submission.objects.all().exclude(Q(submission_status__icontains='solved')).order_by('-timestamp')
#         return qs


@login_required
def the_speaker_unsolved_submissions_list(request):     # UNSOLVED
    submissions = Submission.objects.all().exclude(Q(submission_status__icontains='solved')).order_by('-timestamp')

    # orders = customer.order_set.all()
    # order_count = orders.count()

    my_filter = TableFilter(request.GET, queryset=submissions)
    submissions = my_filter.qs 

    context = {
        'thespeaker_unsolved_submissions_list': submissions, 
        # 'orders': orders, 
        # 'order_count': order_count,
        'my_filter': my_filter
        }
    return render(request, 'submissions/unsolved_submissions.html', context)


# class TheSpeakerSolvedSubmissionsListView(LoginRequiredMixin, ListView):
#     context_object_name = 'thespeaker_solved_submissions_list'
#     template_name = "submissions/solved_submissions.html"
#     # paginate_by = 10

#     def get_queryset(self):
#         # returning whats owned by current user but not solved..
#         qs = Submission.objects.all().filter(Q(submission_status__icontains='solved')).order_by('-timestamp')
#         return qs


@login_required
def the_speaker_solved_submissions_list(request):    # SOLVED
    submissions = Submission.objects.all().filter(Q(submission_status__icontains='solved')).order_by('-timestamp')

    # orders = customer.order_set.all()
    # order_count = orders.count()

    my_filter = TableFilter(request.GET, queryset=submissions)
    submissions = my_filter.qs 

    context = {
        'thespeaker_solved_submissions_list': submissions, 
        # 'orders': orders, 
        # 'order_count': order_count,
        'my_filter': my_filter
        }
    return render(request, 'submissions/solved_submissions.html', context)


class SubmissionsDetailView(LoginRequiredMixin, DetailView):
    template_name = 'submissions/submission_detail.html'
    model = Submission

    # def get_context_data(self, **kwargs):
    #     users = MyUser.objects.all()
    #     super(SubmissionsDetailView, self).get_context_data(**kwargs)
    #     for user in users:
    #         context = {'user': user, }
    #         print("++++++++++++++++++++++++++++++++++++++++++++++++++", context)
    #         return context


# class SubmissionUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
class SubmissionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'submissions/submission_update.html'
    model = Submission
    form_class = SubmissionUpdateForm


class SubmissionStatusSpeakerUpdateView(LoginRequiredMixin, UpdateView):
    """ Here we configured in the templates that Only the speaker will be able
    to change the status of a submission. This view is handling the edition of the status
    """
    template_name = 'submissions/submission_status_update.html'
    model = Submission
    form_class = SubmissionStatusSpeakerUpdateForm
