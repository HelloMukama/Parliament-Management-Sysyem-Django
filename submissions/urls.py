from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required

# from .filters import *
from .views import (SubmissionCreateView,

                    AllSubmissionsListView,
                    SolvedSubmissionsListView,
                    UnsolvedSubmissionsListView,

                    the_speaker_all_submissions_list,
                    # TheSpeakerAllSubmissionsListView,

                    # TheSpeakerUnsolvedSubmissionsListView,
                    the_speaker_unsolved_submissions_list,

                    # TheSpeakerSolvedSubmissionsListView,
                    the_speaker_solved_submissions_list,

                    SubmissionUpdateView,
                    SubmissionStatusSpeakerUpdateView,
                    # SubmissionsDatatableView,
                    SubmissionsDetailView,
                    )

app_name = 'submissions'

urlpatterns = [
    # submissions/

    # create new submission
    path('create/', SubmissionCreateView.as_view(), name='submission_create'),

    # mp
    path('all/me/', AllSubmissionsListView.as_view(), name='all_submissions'),
    path('unresolved/me/', UnsolvedSubmissionsListView.as_view(), name='unsolved_submissions'),
    path('solved/me/', SolvedSubmissionsListView.as_view(), name='solved_submissions'),

    # speaker
    path('all/global/', the_speaker_all_submissions_list, name='thespeaker_all_submissions'),
    # path('all/global/', TheSpeakerAllSubmissionsListView.as_view(), name='thespeaker_all_submissions'),

    # path('unresolved/global/', TheSpeakerUnsolvedSubmissionsListView.as_view(), name='thespeaker_unsolved_submissions'),
    path('unsolved/global/', the_speaker_unsolved_submissions_list, name='thespeaker_unsolved_submissions'),

    # path('solved/global/', TheSpeakerSolvedSubmissionsListView.as_view(), name='thespeaker_solved_submissions'),
    path('solved/global/', the_speaker_solved_submissions_list, name='thespeaker_solved_submissions'),

    # more..
    re_path('^submission-(?P<pk>[0-9]+)/details/$', SubmissionsDetailView.as_view(), name='submission_detail'),

    re_path('^submission-(?P<pk>[0-9]+)/details/update/$', SubmissionUpdateView.as_view(), name='submission_update'),
    
    # CHANGING THE SUBMISSION STATUS
    re_path('^submission-(?P<pk>[0-9]+)/details/update/status/$', SubmissionStatusSpeakerUpdateView.as_view(), name='submission_status_update'),
 


    # path('submissions-list', SubmissionsNonTableListView.as_view(), name='submissions_list_non_table'),   
]


