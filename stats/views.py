# # -*- coding: UTF-8 -*-
# from __future__ import unicode_literals

import sys
sys.path.append('..')  # Adding a higher directory to python modules path.

import functools
import ssl
import submissions
from submissions.models import Submission

from django.conf import settings
from django.utils import timezone
from django.db.models import Count, Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.utils import django_url_fetcher
from django_weasyprint.views import CONTENT_TYPE_PNG, WeasyTemplateResponse

from .mixins import PdfResponseMixin
from .render import Render


###################################################################################
###   THE TABLES >>> TABS 1, 2 & 3                                              ###
###################################################################################
# Viewable on  http://127.0.0.1:8000/stats/cat-nums/
class GeneralSubmissionCountForTableView(LoginRequiredMixin, ListView):
    template_name = 'stats/submissions_cat_n_region_count.html'

    def get_queryset(self):
        return Submission.objects.all()

    def get_context_data(self, *args, object_list=None, **kwargs):

        # Agriculture
        agric_north = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                                Q(region__icontains="Northern")).count()
        agric_east = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                               Q(region__icontains="Eastern")).count()
        agric_south = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                                Q(region__icontains="Southern")).count()
        agric_central = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                                  Q(region__icontains="Central")).count()
        agric_west = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                               Q(region__icontains="Western")).count()

        # Education
        educ_north = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                               Q(region__icontains="Northern")).count()
        educ_east = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                              Q(region__icontains="Eastern")).count()
        educ_south = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                               Q(region__icontains="Southern")).count()
        educ_central = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                                 Q(region__icontains="Central")).count()
        educ_west = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                              Q(region__icontains="Western")).count()

        # Health
        health_north = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                 Q(region__icontains="Northern")).count()
        health_east = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                Q(region__icontains="Eastern")).count()
        health_south = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                 Q(region__icontains="Southern")).count()
        health_central = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                   Q(region__icontains="Central")).count()
        health_west = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                Q(region__icontains="Western")).count()

        # Industry
        ind_north = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                              Q(region__icontains="Northern")).count()
        ind_east = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                             Q(region__icontains="Eastern")).count()
        ind_south = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                              Q(region__icontains="Southern")).count()
        ind_central = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                                Q(region__icontains="Central")).count()
        ind_west = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                             Q(region__icontains="Western")).count()

        # Security
        sec_north = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                              Q(region__icontains="Northern")).count()
        sec_east = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                             Q(region__icontains="Eastern")).count()
        sec_south = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                              Q(region__icontains="Southern")).count()
        sec_central = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                                Q(region__icontains="Central")).count()
        sec_west = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                             Q(region__icontains="Western")).count()

        # Technology
        tech_north = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                               Q(region__icontains="Northern")).count()
        tech_east = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                              Q(region__icontains="Eastern")).count()
        tech_south = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                               Q(region__icontains="Southern")).count()
        tech_central = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                                 Q(region__icontains="Central")).count()
        tech_west = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                              Q(region__icontains="Western")).count()

        # Tourism
        tour_north = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                               Q(region__icontains="Northern")).count()
        tour_east = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                              Q(region__icontains="Eastern")).count()
        tour_south = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                               Q(region__icontains="Southern")).count()
        tour_central = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                                 Q(region__icontains="Central")).count()
        tour_west = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                              Q(region__icontains="Western")).count()

        # Others
        others_north = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                 Q(region__icontains="Northern")).count()
        others_east = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                Q(region__icontains="Eastern")).count()
        others_south = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                 Q(region__icontains="Southern")).count()
        others_central = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                   Q(region__icontains="Central")).count()
        others_west = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                Q(region__icontains="Western")).count()

        # Totals >> ROWS
        agric_total = agric_north + agric_east + agric_central + agric_south + agric_west
        educ_total = educ_north + educ_east + educ_central + educ_south + educ_west
        health_total = health_north + health_east + health_central + health_south + health_west
        ind_total = ind_north + ind_east + ind_central + ind_south + ind_west
        sec_total = sec_north + sec_east + sec_central + sec_south + sec_west
        tech_total = tech_north + tech_east + tech_central + tech_south + tech_west
        tour_total = tour_north + tour_east + tour_central + tour_south + tour_west
        others_total = others_north + others_east + others_central + others_south + others_west

        # Totals >> cols
        north_total = agric_north + educ_north + health_north + ind_north + sec_north + tech_north + tour_north + others_north
        east_total = agric_east + educ_east + health_east + ind_east + sec_east + tech_east + tour_east + others_east
        central_total = agric_central + educ_central + health_central + ind_central + sec_central + tech_central + tour_central + others_central
        south_total = agric_south + educ_south + health_south + ind_south + sec_south + tech_south + tour_south + others_south
        west_total = agric_west + educ_west + health_west + ind_west + sec_west + tech_west + tour_west + others_west

        total_subs_as_per_cats = agric_total + educ_total + health_total + ind_total + sec_total + tech_total + tour_total + others_total
        total_subs_as_per_regions = north_total + east_total + central_total + south_total + west_total

        context = super(GeneralSubmissionCountForTableView, self).get_context_data(**kwargs)
        context = {
            # Agriculture
            'agric_north': agric_north,
            'agric_east': agric_east,
            'agric_south': agric_south,
            'agric_central': agric_central,
            'agric_west': agric_west,

            # Education
            'educ_north': educ_north,
            'educ_east': educ_east,
            'educ_south': educ_south,
            'educ_central': educ_central,
            'educ_west': educ_west,

            # Health
            'health_north': health_north,
            'health_east': health_east,
            'health_south': health_south,
            'health_central': health_central,
            'health_west': health_west,

            # Industry
            'ind_north': ind_north,
            'ind_east': ind_east,
            'ind_south': ind_south,
            'ind_central': ind_central,
            'ind_west': ind_west,

            # Security
            'sec_north': sec_north,
            'sec_east': sec_east,
            'sec_south': sec_south,
            'sec_central': sec_central,
            'sec_west': sec_west,

            # Technology
            'tech_north': tech_north,
            'tech_east': tech_east,
            'tech_south': tech_south,
            'tech_central': tech_central,
            'tech_west': tech_west,

            # Tourism
            'tour_north': tour_north,
            'tour_east': tour_east,
            'tour_south': tour_south,
            'tour_central': tour_central,
            'tour_west': tour_west,

            # Others
            'others_north': others_north,
            'others_east': others_east,
            'others_south': others_south,
            'others_central': others_central,
            'others_west': others_west,

            # TOTALS >>
            # rows
            "agric_total": agric_total,
            "educ_total": educ_total,
            "health_total": health_total,
            "ind_total": ind_total,
            "sec_total": sec_total,
            "tech_total": tech_total,
            "tour_total": tour_total,
            "others_total": others_total,

            # cols
            "north_total": north_total,
            "east_total": east_total,
            "central_total": central_total,
            "south_total": south_total,
            "west_total": west_total,

            'total_subs_as_per_cats': total_subs_as_per_cats,
            'total_subs_as_per_regions': total_subs_as_per_regions,
        }
        return context   # end table tabs 1,2,3


##########################################################################
#                     THE DASHBOARD >> MP & thespeaker                   #
##########################################################################
@login_required(login_url='/account/login/')
def render_all_data_to_dash(request):   # MP View
    template_name = 'stats/dashboard.html'

    # the dashboard Column/line/bar-Chart 3 OF THEM WILL USE THE SAME CONTEXT DATA
    mp_bar_categories = []
    mp_bar_values = []

    # This is for the piechart showing on the dashboard
    mp_pie_categories = []
    mp_pie_data = []

    # This is for the 3D chart showing on the dashboard
    mp_funnel_categories = []
    mp_funnel_data = []

    # This is for the 4 cards on top of the dashboard. Counting the status numbers
    """get the count of all the submissions-- solved, unsolved and inprogres"""
    mp_cards_total = Submission.objects.all().filter(profile__user=request.user).count()  # count those of current user
    mp_cards_pending = Submission.objects.all().filter(profile__user=request.user).filter(submission_status__icontains='pending').count()
    mp_cards_inprogress = Submission.objects.all().filter(profile__user=request.user).filter(submission_status__icontains='inprogress').count()
    mp_cards_solved = Submission.objects.all().filter(profile__user=request.user).filter(submission_status__icontains='solved').count()
    mp_cards_dataset = Submission.objects.filter(profile__user=request.user).values('submission_category').annotate(total=Count('submission_status'), solved=Count('submission_status', filter=Q(submission_status='solved')), unsolved=Count('submission_status', filter=Q(submission_status='unsolved')), inprogress=Count('submission_status', filter=Q(submission_status='inprogres'))).order_by('-timestamp')


    # ANALYSING EACH OF THE CATEGORIES INDIVIDUALY ##################  MP  #########################3

    # Agriculture
    mp_agric_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") & 
                                          Q(region__icontains="Northern")).count()
    mp_agric_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") & 
                                          Q(region__icontains="Eastern")).count()
    mp_agric_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") &
                                            Q(region__icontains="Southern")).count()
    mp_agric_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") & 
                                              Q(region__icontains="Central")).count()
    mp_agric_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") &
                                                Q(region__icontains="Western")).count()

    # Education
    mp_educ_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                           Q(region__icontains="Northern")).count()
    mp_educ_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                          Q(region__icontains="Eastern")).count()
    mp_educ_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                           Q(region__icontains="Southern")).count()
    mp_educ_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                             Q(region__icontains="Central")).count()
    mp_educ_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                          Q(region__icontains="Western")).count()

    # Health
    mp_health_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                             Q(region__icontains="Northern")).count()
    mp_health_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                            Q(region__icontains="Eastern")).count()
    mp_health_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                             Q(region__icontains="Southern")).count()
    mp_health_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                               Q(region__icontains="Central")).count()
    mp_health_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                            Q(region__icontains="Western")).count()

    # Industry
    mp_ind_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                          Q(region__icontains="Northern")).count()
    mp_ind_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                         Q(region__icontains="Eastern")).count()
    mp_ind_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                          Q(region__icontains="Southern")).count()
    mp_ind_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                            Q(region__icontains="Central")).count()
    mp_ind_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                         Q(region__icontains="Western")).count()

    # Security
    mp_sec_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                          Q(region__icontains="Northern")).count()
    mp_sec_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                         Q(region__icontains="Eastern")).count()
    mp_sec_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                          Q(region__icontains="Southern")).count()
    mp_sec_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                            Q(region__icontains="Central")).count()
    mp_sec_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                         Q(region__icontains="Western")).count()

    # Technology
    mp_tech_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                           Q(region__icontains="Northern")).count()
    mp_tech_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                          Q(region__icontains="Eastern")).count()
    mp_tech_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                           Q(region__icontains="Southern")).count()
    mp_tech_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                             Q(region__icontains="Central")).count()
    mp_tech_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                          Q(region__icontains="Western")).count()

    # Tourism
    mp_tour_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                           Q(region__icontains="Northern")).count()
    mp_tour_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                          Q(region__icontains="Eastern")).count()
    mp_tour_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                           Q(region__icontains="Southern")).count()
    mp_tour_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                             Q(region__icontains="Central")).count()
    mp_tour_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                          Q(region__icontains="Western")).count()

    # Others
    mp_others_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                             Q(region__icontains="Northern")).count()
    mp_others_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                            Q(region__icontains="Eastern")).count()
    mp_others_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                             Q(region__icontains="Southern")).count()
    mp_others_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                               Q(region__icontains="Central")).count()
    mp_others_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                            Q(region__icontains="Western")).count()

    # Totals >> ROWS
    mp_agric_total = mp_agric_north + mp_agric_east + mp_agric_central + mp_agric_south + mp_agric_west
    mp_educ_total = mp_educ_north + mp_educ_east + mp_educ_central + mp_educ_south + mp_educ_west
    mp_health_total = mp_health_north + mp_health_east + mp_health_central + mp_health_south + mp_health_west
    mp_ind_total = mp_ind_north + mp_ind_east + mp_ind_central + mp_ind_south + mp_ind_west
    mp_sec_total = mp_sec_north + mp_sec_east + mp_sec_central + mp_sec_south + mp_sec_west
    mp_tech_total = mp_tech_north + mp_tech_east + mp_tech_central + mp_tech_south + mp_tech_west
    mp_tour_total = mp_tour_north + mp_tour_east + mp_tour_central + mp_tour_south + mp_tour_west
    mp_others_total = mp_others_north + mp_others_east + mp_others_central + mp_others_south + mp_others_west

    cats = ["Agriculture", "Education", "Health", "Industry", "Security", "Technology", "Tourism", "Others"]
    mp_the_totals = [mp_agric_total, mp_educ_total, mp_health_total, mp_ind_total, mp_sec_total, mp_tech_total, mp_tour_total, mp_others_total]

    for cat in cats:
        mp_bar_categories.append(cat)
    for total in mp_the_totals:
        mp_bar_values.append(total)

    # pie chart dashboard
    mp_pie_total_agriculture = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Agriculture").count()
    mp_pie_total_education = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Education").count()
    mp_pie_total_health = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Health").count()
    mp_pie_total_industry = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Industry").count()
    mp_pie_total_security = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Security").count()
    mp_pie_total_technology = Submission.objects.filter(profile__user=request.user).filter(submission_category__iexact="Technology").count()
    mp_pie_total_tourism = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Tourism").count()
    mp_pie_total_others = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Others").count()

    # 3D chart dashboard
    mp_funnel_total_agriculture = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Agriculture").count()
    mp_funnel_total_education = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Education").count()
    mp_funnel_total_health = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Health").count()
    mp_funnel_total_industry = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Industry").count()
    mp_funnel_total_security = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Security").count()
    mp_funnel_total_technology = Submission.objects.filter(profile__user=request.user).filter(submission_category__iexact="Technology").count()
    mp_funnel_total_tourism = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Tourism").count()
    mp_funnel_total_others = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Others").count()

    qs = Submission.objects.all()
    for x in qs:
        mp_pie_categories.append(x.submission_category)


    # THE SPEAKER'S DASH CONFIG

    thespeaker_categories = []
    thespeaker_values = []
    arr_regions_thespeaker = []
    arr_region_totals_thespeaker = []
    n_total_values_thespeaker = []
    e_total_values_thespeaker = []
    c_total_values_thespeaker = []
    s_total_values_thespeaker = []
    w_total_values_thespeaker = []

    total_subs_thespeaker = Submission.objects.all().count()  # count those of current user
    pending_thespeaker = Submission.objects.all().filter(submission_status__icontains='pending').count()
    inprogress_thespeaker = Submission.objects.all().filter(submission_status__icontains='inprogress').count()
    solved_thespeaker = Submission.objects.all().filter(submission_status__icontains='solved').count()
    dataset_thespeaker = Submission.objects.all().values('submission_category').annotate(
        total=Count('submission_status'),
        solved=Count('submission_status', filter=Q(submission_status='solved')),
        unsolved=Count('submission_status', filter=Q(submission_status='unsolved')), 
        inprogress=Count('submission_status', filter=Q(submission_status='inprogres'))).order_by('-timestamp')

    # Agriculture
    thespeaker_agric_north = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                            Q(region__icontains="Northern")).count()
    thespeaker_agric_east = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                           Q(region__icontains="Eastern")).count()
    thespeaker_agric_south = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                            Q(region__icontains="Southern")).count()
    thespeaker_agric_central = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                              Q(region__icontains="Central")).count()
    thespeaker_agric_west = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                           Q(region__icontains="Western")).count()

    # Education
    thespeaker_educ_north = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                           Q(region__icontains="Northern")).count()
    thespeaker_educ_east = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                          Q(region__icontains="Eastern")).count()
    thespeaker_educ_south = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                           Q(region__icontains="Southern")).count()
    thespeaker_educ_central = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                             Q(region__icontains="Central")).count()
    thespeaker_educ_west = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                          Q(region__icontains="Western")).count()

    # Health
    thespeaker_health_north = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                             Q(region__icontains="Northern")).count()
    thespeaker_health_east = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                            Q(region__icontains="Eastern")).count()
    thespeaker_health_south = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                             Q(region__icontains="Southern")).count()
    thespeaker_health_central = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                               Q(region__icontains="Central")).count()
    thespeaker_health_west = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                            Q(region__icontains="Western")).count()

    # Industry
    thespeaker_ind_north = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                          Q(region__icontains="Northern")).count()
    thespeaker_ind_east = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                         Q(region__icontains="Eastern")).count()
    thespeaker_ind_south = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                          Q(region__icontains="Southern")).count()
    thespeaker_ind_central = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                            Q(region__icontains="Central")).count()
    thespeaker_ind_west = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                         Q(region__icontains="Western")).count()

    # Security
    thespeaker_sec_north = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                          Q(region__icontains="Northern")).count()
    thespeaker_sec_east = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                         Q(region__icontains="Eastern")).count()
    thespeaker_sec_south = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                          Q(region__icontains="Southern")).count()
    thespeaker_sec_central = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                            Q(region__icontains="Central")).count()
    thespeaker_sec_west = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                         Q(region__icontains="Western")).count()

    # Technology
    thespeaker_tech_north = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                           Q(region__icontains="Northern")).count()
    thespeaker_tech_east = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                          Q(region__icontains="Eastern")).count()
    thespeaker_tech_south = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                           Q(region__icontains="Southern")).count()
    thespeaker_tech_central = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                             Q(region__icontains="Central")).count()
    thespeaker_tech_west = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                          Q(region__icontains="Western")).count()

    # Tourism
    thespeaker_tour_north = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                           Q(region__icontains="Northern")).count()
    thespeaker_tour_east = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                          Q(region__icontains="Eastern")).count()
    thespeaker_tour_south = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                           Q(region__icontains="Southern")).count()
    thespeaker_tour_central = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                             Q(region__icontains="Central")).count()
    thespeaker_tour_west = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                          Q(region__icontains="Western")).count()

    # Others
    thespeaker_others_north = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                             Q(region__icontains="Northern")).count()
    thespeaker_others_east = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                            Q(region__icontains="Eastern")).count()
    thespeaker_others_south = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                             Q(region__icontains="Southern")).count()
    thespeaker_others_central = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                               Q(region__icontains="Central")).count()
    thespeaker_others_west = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                            Q(region__icontains="Western")).count()

    # Totals >> ROWS
    thespeaker_agric_total = thespeaker_agric_north + thespeaker_agric_east + thespeaker_agric_central + thespeaker_agric_south + thespeaker_agric_west
    thespeaker_educ_total = thespeaker_educ_north + thespeaker_educ_east + thespeaker_educ_central + thespeaker_educ_south + thespeaker_educ_west
    thespeaker_health_total = thespeaker_health_north + thespeaker_health_east + thespeaker_health_central + thespeaker_health_south + thespeaker_health_west
    thespeaker_ind_total = thespeaker_ind_north + thespeaker_ind_east + thespeaker_ind_central + thespeaker_ind_south + thespeaker_ind_west
    thespeaker_sec_total = thespeaker_sec_north + thespeaker_sec_east + thespeaker_sec_central + thespeaker_sec_south + thespeaker_sec_west
    thespeaker_tech_total = thespeaker_tech_north + thespeaker_tech_east + thespeaker_tech_central + thespeaker_tech_south + thespeaker_tech_west
    thespeaker_tour_total = thespeaker_tour_north + thespeaker_tour_east + thespeaker_tour_central + thespeaker_tour_south + thespeaker_tour_west
    thespeaker_others_total = thespeaker_others_north + thespeaker_others_east + thespeaker_others_central + thespeaker_others_south + thespeaker_others_west

    # Totals >> cols
    north_total = thespeaker_agric_north + thespeaker_educ_north + thespeaker_health_north + thespeaker_ind_north + thespeaker_sec_north + thespeaker_tech_north + thespeaker_tour_north + thespeaker_others_north
    east_total = thespeaker_agric_east + thespeaker_educ_east + thespeaker_health_east + thespeaker_ind_east + thespeaker_sec_east + thespeaker_tech_east + thespeaker_tour_east + thespeaker_others_east
    central_total = thespeaker_agric_central + thespeaker_educ_central + thespeaker_health_central + thespeaker_ind_central + thespeaker_sec_central + thespeaker_tech_central + thespeaker_tour_central + thespeaker_others_central
    south_total = thespeaker_agric_south + thespeaker_educ_south + thespeaker_health_south + thespeaker_ind_south + thespeaker_sec_south + thespeaker_tech_south + thespeaker_tour_south + thespeaker_others_south
    west_total = thespeaker_agric_west + thespeaker_educ_west + thespeaker_health_west + thespeaker_ind_west + thespeaker_sec_west + thespeaker_tech_west + thespeaker_tour_west + thespeaker_others_west

    cats = ["Agriculture", "Education", "Health", "Industry", "Security", "Technology", "Tourism", "Others"]
    thespeaker_the_totals = [thespeaker_agric_total, thespeaker_educ_total, thespeaker_health_total, thespeaker_ind_total, thespeaker_sec_total, thespeaker_tech_total, thespeaker_tour_total, thespeaker_others_total]

    regions_list = ["Northern", "Eastern", "Central", "Southern", "Western"]
    regions_totals = [north_total, east_total, central_total, south_total, west_total]
    
    north_total_list = [thespeaker_agric_north, thespeaker_educ_north, thespeaker_health_north, thespeaker_ind_north, thespeaker_sec_north, thespeaker_tech_north, thespeaker_tour_north, thespeaker_others_north]
    east_total_list = [thespeaker_agric_east, thespeaker_educ_east, thespeaker_health_east, thespeaker_ind_east, thespeaker_sec_east, thespeaker_tech_east, thespeaker_tour_east, thespeaker_others_east]
    central_total_list = [thespeaker_agric_central, thespeaker_educ_central, thespeaker_health_central, thespeaker_ind_central, thespeaker_sec_central, thespeaker_tech_central, thespeaker_tour_central, thespeaker_others_central]
    south_total_list = [thespeaker_agric_south, thespeaker_educ_south, thespeaker_health_south, thespeaker_ind_south, thespeaker_sec_south, thespeaker_tech_south, thespeaker_tour_south, thespeaker_others_south]
    west_total_list = [thespeaker_agric_west, thespeaker_educ_west, thespeaker_health_west, thespeaker_ind_west, thespeaker_sec_west, thespeaker_tech_west, thespeaker_tour_west, thespeaker_others_west]
    
    for r_item in regions_list:
        arr_regions_thespeaker.append(r_item)
    for r_total in regions_totals:
        arr_region_totals_thespeaker.append(r_total)
    for cat in cats:
        thespeaker_categories.append(cat)
    for total in thespeaker_the_totals:
        thespeaker_values.append(total)

    for n_total in north_total_list:
        n_total_values_thespeaker.append(n_total)
    for e_total in east_total_list:
        e_total_values_thespeaker.append(e_total)
    for c_total in central_total_list:
        c_total_values_thespeaker.append(c_total)
    for s_total in south_total_list:
        s_total_values_thespeaker.append(s_total)
    for w_total in west_total_list:
        w_total_values_thespeaker.append(w_total)


    # rendering all the stuff to the dashboard
    context_dash = {

        # *********** MP *****************

        # the 4 top cards
        'mp_cards_total': mp_cards_total,
        'mp_cards_solved': mp_cards_solved,
        'mp_cards_pending': mp_cards_pending,
        'mp_cards_inprogress': mp_cards_inprogress,
        'mp_cards_dataset': mp_cards_dataset,

        # the bar/column charts
        'mp_bar_categories': mp_bar_categories,
        'mp_bar_values': mp_bar_values,

        # piechart
        'mp_pie_categories': mp_pie_categories,
        'mp_pie_data': mp_pie_data,

        'mp_pie_total_agriculture': mp_pie_total_agriculture,
        'mp_pie_total_education': mp_pie_total_education,
        'mp_pie_total_health': mp_pie_total_health,
        'mp_pie_total_industry': mp_pie_total_industry,
        'mp_pie_total_security': mp_pie_total_security,
        'mp_pie_total_technology': mp_pie_total_technology,
        'mp_pie_total_tourism': mp_pie_total_tourism,
        'mp_pie_total_others': mp_pie_total_others,

        # 3D chart on the dashboard
        'mp_funnel_total_agriculture': mp_funnel_total_agriculture,
        'mp_funnel_total_education': mp_funnel_total_education,
        'mp_funnel_total_health': mp_funnel_total_health,
        'mp_funnel_total_industry': mp_funnel_total_industry,
        'mp_funnel_total_security': mp_funnel_total_security,
        'mp_funnel_total_technology': mp_funnel_total_technology,
        'mp_funnel_total_tourism': mp_funnel_total_tourism,
        'mp_funnel_total_others': mp_funnel_total_others,


        # ********************** THE SPEAKER **********************
        # the 4 top cards
        'total_subs_thespeaker': total_subs_thespeaker,
        'solved_thespeaker': solved_thespeaker,
        'pending_thespeaker': pending_thespeaker,
        'inprogress_thespeaker': inprogress_thespeaker,
        'dataset_thespeaker': dataset_thespeaker,

        # this is handling the bar/column/line charts
        'thespeaker_categories': thespeaker_categories, 
        'thespeaker_values': thespeaker_values,

        'thespeaker_agric_total': thespeaker_agric_total,
        'thespeaker_educ_total': thespeaker_educ_total,
        'thespeaker_health_total': thespeaker_health_total,
        'thespeaker_ind_total': thespeaker_ind_total,
        'thespeaker_sec_total': thespeaker_sec_total,
        'thespeaker_tech_total': thespeaker_tech_total,
        'thespeaker_tour_total': thespeaker_tour_total,
        'thespeaker_others_total': thespeaker_others_total,

        # this is for the global graph of cat and region vs the numbers
        'arr_regions_thespeaker': arr_regions_thespeaker,
        'arr_region_totals_thespeaker': arr_region_totals_thespeaker,
        'n_total_values_thespeaker': n_total_values_thespeaker,
        'e_total_values_thespeaker': e_total_values_thespeaker,
        'c_total_values_thespeaker': c_total_values_thespeaker,
        's_total_values_thespeaker': s_total_values_thespeaker,
        'w_total_values_thespeaker': w_total_values_thespeaker
    }
       
    return render(request, template_name, context_dash)     # Working # MP # THE SPEAKER   # END


##########################################################################
#                     THE CHARTS PAGE >> MP // thespeaker                #
##########################################################################
@login_required(login_url='/account/login/')
def render_all_data_for_mp_charts_view(request):
    template_name = 'stats/charts_view.html'

    # the dashboard Column/line/bar-Chart 3 OF THEM WILL USE THE SAME CONTEXT DATA
    mp_bar_categories = []
    mp_bar_values = []

    # This is for the piechart showing on the dashboard
    mp_pie_categories = []
    mp_pie_data = []

    # This is for the 3D chart showing on the dashboard
    mp_funnel_categories = []
    mp_funnel_data = []

    # This is for the 4 cards on top of the dashboard. Counting the status numbers
    """get the count of all the submissions-- solved, unsolved and inprogres"""
    mp_cards_total = Submission.objects.all().filter(profile__user=request.user).count()  # count those of current user
    mp_cards_pending = Submission.objects.all().filter(profile__user=request.user).filter(submission_status__icontains='pending').count()
    mp_cards_inprogress = Submission.objects.all().filter(profile__user=request.user).filter(submission_status__icontains='inprogress').count()
    mp_cards_solved = Submission.objects.all().filter(profile__user=request.user).filter(submission_status__icontains='solved').count()
    mp_cards_dataset = Submission.objects.filter(profile__user=request.user).values('submission_category').annotate(total=Count('submission_status'), solved=Count('submission_status', filter=Q(submission_status='solved')), unsolved=Count('submission_status', filter=Q(submission_status='unsolved')), inprogress=Count('submission_status', filter=Q(submission_status='inprogres'))).order_by('-timestamp')


    # ANALYSING EACH OF THE CATEGORIES INDIVIDUALY ##################  MP  #########################3

    # Agriculture
    mp_agric_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") & 
                                          Q(region__icontains="Northern")).count()
    mp_agric_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") & 
                                          Q(region__icontains="Eastern")).count()
    mp_agric_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") &
                                            Q(region__icontains="Southern")).count()
    mp_agric_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") & 
                                              Q(region__icontains="Central")).count()
    mp_agric_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Agriculture") &
                                                Q(region__icontains="Western")).count()

    # Education
    mp_educ_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                           Q(region__icontains="Northern")).count()
    mp_educ_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                          Q(region__icontains="Eastern")).count()
    mp_educ_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                           Q(region__icontains="Southern")).count()
    mp_educ_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                             Q(region__icontains="Central")).count()
    mp_educ_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Education") &
                                          Q(region__icontains="Western")).count()

    # Health
    mp_health_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                             Q(region__icontains="Northern")).count()
    mp_health_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                            Q(region__icontains="Eastern")).count()
    mp_health_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                             Q(region__icontains="Southern")).count()
    mp_health_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                               Q(region__icontains="Central")).count()
    mp_health_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Health") &
                                            Q(region__icontains="Western")).count()

    # Industry
    mp_ind_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                          Q(region__icontains="Northern")).count()
    mp_ind_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                         Q(region__icontains="Eastern")).count()
    mp_ind_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                          Q(region__icontains="Southern")).count()
    mp_ind_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                            Q(region__icontains="Central")).count()
    mp_ind_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Industry") &
                                         Q(region__icontains="Western")).count()

    # Security
    mp_sec_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                          Q(region__icontains="Northern")).count()
    mp_sec_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                         Q(region__icontains="Eastern")).count()
    mp_sec_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                          Q(region__icontains="Southern")).count()
    mp_sec_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                            Q(region__icontains="Central")).count()
    mp_sec_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Security") &
                                         Q(region__icontains="Western")).count()

    # Technology
    mp_tech_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                           Q(region__icontains="Northern")).count()
    mp_tech_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                          Q(region__icontains="Eastern")).count()
    mp_tech_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                           Q(region__icontains="Southern")).count()
    mp_tech_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                             Q(region__icontains="Central")).count()
    mp_tech_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Technology") &
                                          Q(region__icontains="Western")).count()

    # Tourism
    mp_tour_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                           Q(region__icontains="Northern")).count()
    mp_tour_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                          Q(region__icontains="Eastern")).count()
    mp_tour_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                           Q(region__icontains="Southern")).count()
    mp_tour_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                             Q(region__icontains="Central")).count()
    mp_tour_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Tourism") &
                                          Q(region__icontains="Western")).count()

    # Others
    mp_others_north = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                             Q(region__icontains="Northern")).count()
    mp_others_east = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                            Q(region__icontains="Eastern")).count()
    mp_others_south = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                             Q(region__icontains="Southern")).count()
    mp_others_central = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                               Q(region__icontains="Central")).count()
    mp_others_west = Submission.objects.filter(profile__user=request.user).filter(Q(submission_category__icontains="Others") &
                                            Q(region__icontains="Western")).count()

    # Totals >> ROWS
    mp_agric_total = mp_agric_north + mp_agric_east + mp_agric_central + mp_agric_south + mp_agric_west
    mp_educ_total = mp_educ_north + mp_educ_east + mp_educ_central + mp_educ_south + mp_educ_west
    mp_health_total = mp_health_north + mp_health_east + mp_health_central + mp_health_south + mp_health_west
    mp_ind_total = mp_ind_north + mp_ind_east + mp_ind_central + mp_ind_south + mp_ind_west
    mp_sec_total = mp_sec_north + mp_sec_east + mp_sec_central + mp_sec_south + mp_sec_west
    mp_tech_total = mp_tech_north + mp_tech_east + mp_tech_central + mp_tech_south + mp_tech_west
    mp_tour_total = mp_tour_north + mp_tour_east + mp_tour_central + mp_tour_south + mp_tour_west
    mp_others_total = mp_others_north + mp_others_east + mp_others_central + mp_others_south + mp_others_west

    cats = ["Agriculture", "Education", "Health", "Industry", "Security", "Technology", "Tourism", "Others"]
    mp_the_totals = [mp_agric_total, mp_educ_total, mp_health_total, mp_ind_total, mp_sec_total, mp_tech_total, mp_tour_total, mp_others_total]

    for cat in cats:
        mp_bar_categories.append(cat)
    for total in mp_the_totals:
        mp_bar_values.append(total)

    # pie chart dashboard
    mp_pie_total_agriculture = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Agriculture").count()
    mp_pie_total_education = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Education").count()
    mp_pie_total_health = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Health").count()
    mp_pie_total_industry = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Industry").count()
    mp_pie_total_security = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Security").count()
    mp_pie_total_technology = Submission.objects.filter(profile__user=request.user).filter(submission_category__iexact="Technology").count()
    mp_pie_total_tourism = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Tourism").count()
    mp_pie_total_others = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Others").count()

    # 3D chart dashboard
    mp_funnel_total_agriculture = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Agriculture").count()
    mp_funnel_total_education = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Education").count()
    mp_funnel_total_health = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Health").count()
    mp_funnel_total_industry = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Industry").count()
    mp_funnel_total_security = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Security").count()
    mp_funnel_total_technology = Submission.objects.filter(profile__user=request.user).filter(submission_category__iexact="Technology").count()
    mp_funnel_total_tourism = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Tourism").count()
    mp_funnel_total_others = Submission.objects.filter(profile__user=request.user).filter(submission_category__icontains="Others").count()

    qs = Submission.objects.all()
    for x in qs:
        mp_pie_categories.append(x.submission_category)


    # THE SPEAKER'S DASH CONFIG

    thespeaker_categories = []
    thespeaker_values = []
    arr_regions_thespeaker = []
    arr_region_totals_thespeaker = []
    n_total_values_thespeaker = []
    e_total_values_thespeaker = []
    c_total_values_thespeaker = []
    s_total_values_thespeaker = []
    w_total_values_thespeaker = []

    total_subs_thespeaker = Submission.objects.all().count()  # count those of current user
    pending_thespeaker = Submission.objects.all().filter(submission_status__icontains='pending').count()
    inprogress_thespeaker = Submission.objects.all().filter(submission_status__icontains='inprogress').count()
    solved_thespeaker = Submission.objects.all().filter(submission_status__icontains='solved').count()
    dataset_thespeaker = Submission.objects.all().values('submission_category').annotate(
        total=Count('submission_status'),
        solved=Count('submission_status', filter=Q(submission_status='solved')),
        unsolved=Count('submission_status', filter=Q(submission_status='unsolved')), 
        inprogress=Count('submission_status', filter=Q(submission_status='inprogres'))).order_by('-timestamp')

    # Agriculture
    thespeaker_agric_north = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                            Q(region__icontains="Northern")).count()
    thespeaker_agric_east = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                           Q(region__icontains="Eastern")).count()
    thespeaker_agric_south = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                            Q(region__icontains="Southern")).count()
    thespeaker_agric_central = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                              Q(region__icontains="Central")).count()
    thespeaker_agric_west = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                           Q(region__icontains="Western")).count()

    # Education
    thespeaker_educ_north = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                           Q(region__icontains="Northern")).count()
    thespeaker_educ_east = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                          Q(region__icontains="Eastern")).count()
    thespeaker_educ_south = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                           Q(region__icontains="Southern")).count()
    thespeaker_educ_central = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                             Q(region__icontains="Central")).count()
    thespeaker_educ_west = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                          Q(region__icontains="Western")).count()

    # Health
    thespeaker_health_north = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                             Q(region__icontains="Northern")).count()
    thespeaker_health_east = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                            Q(region__icontains="Eastern")).count()
    thespeaker_health_south = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                             Q(region__icontains="Southern")).count()
    thespeaker_health_central = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                               Q(region__icontains="Central")).count()
    thespeaker_health_west = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                            Q(region__icontains="Western")).count()

    # Industry
    thespeaker_ind_north = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                          Q(region__icontains="Northern")).count()
    thespeaker_ind_east = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                         Q(region__icontains="Eastern")).count()
    thespeaker_ind_south = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                          Q(region__icontains="Southern")).count()
    thespeaker_ind_central = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                            Q(region__icontains="Central")).count()
    thespeaker_ind_west = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                         Q(region__icontains="Western")).count()

    # Security
    thespeaker_sec_north = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                          Q(region__icontains="Northern")).count()
    thespeaker_sec_east = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                         Q(region__icontains="Eastern")).count()
    thespeaker_sec_south = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                          Q(region__icontains="Southern")).count()
    thespeaker_sec_central = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                            Q(region__icontains="Central")).count()
    thespeaker_sec_west = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                         Q(region__icontains="Western")).count()

    # Technology
    thespeaker_tech_north = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                           Q(region__icontains="Northern")).count()
    thespeaker_tech_east = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                          Q(region__icontains="Eastern")).count()
    thespeaker_tech_south = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                           Q(region__icontains="Southern")).count()
    thespeaker_tech_central = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                             Q(region__icontains="Central")).count()
    thespeaker_tech_west = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                          Q(region__icontains="Western")).count()

    # Tourism
    thespeaker_tour_north = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                           Q(region__icontains="Northern")).count()
    thespeaker_tour_east = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                          Q(region__icontains="Eastern")).count()
    thespeaker_tour_south = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                           Q(region__icontains="Southern")).count()
    thespeaker_tour_central = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                             Q(region__icontains="Central")).count()
    thespeaker_tour_west = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                          Q(region__icontains="Western")).count()

    # Others
    thespeaker_others_north = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                             Q(region__icontains="Northern")).count()
    thespeaker_others_east = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                            Q(region__icontains="Eastern")).count()
    thespeaker_others_south = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                             Q(region__icontains="Southern")).count()
    thespeaker_others_central = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                               Q(region__icontains="Central")).count()
    thespeaker_others_west = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                            Q(region__icontains="Western")).count()

    # Totals >> ROWS
    thespeaker_agric_total = thespeaker_agric_north + thespeaker_agric_east + thespeaker_agric_central + thespeaker_agric_south + thespeaker_agric_west
    thespeaker_educ_total = thespeaker_educ_north + thespeaker_educ_east + thespeaker_educ_central + thespeaker_educ_south + thespeaker_educ_west
    thespeaker_health_total = thespeaker_health_north + thespeaker_health_east + thespeaker_health_central + thespeaker_health_south + thespeaker_health_west
    thespeaker_ind_total = thespeaker_ind_north + thespeaker_ind_east + thespeaker_ind_central + thespeaker_ind_south + thespeaker_ind_west
    thespeaker_sec_total = thespeaker_sec_north + thespeaker_sec_east + thespeaker_sec_central + thespeaker_sec_south + thespeaker_sec_west
    thespeaker_tech_total = thespeaker_tech_north + thespeaker_tech_east + thespeaker_tech_central + thespeaker_tech_south + thespeaker_tech_west
    thespeaker_tour_total = thespeaker_tour_north + thespeaker_tour_east + thespeaker_tour_central + thespeaker_tour_south + thespeaker_tour_west
    thespeaker_others_total = thespeaker_others_north + thespeaker_others_east + thespeaker_others_central + thespeaker_others_south + thespeaker_others_west

    # Totals >> cols
    north_total = thespeaker_agric_north + thespeaker_educ_north + thespeaker_health_north + thespeaker_ind_north + thespeaker_sec_north + thespeaker_tech_north + thespeaker_tour_north + thespeaker_others_north
    east_total = thespeaker_agric_east + thespeaker_educ_east + thespeaker_health_east + thespeaker_ind_east + thespeaker_sec_east + thespeaker_tech_east + thespeaker_tour_east + thespeaker_others_east
    central_total = thespeaker_agric_central + thespeaker_educ_central + thespeaker_health_central + thespeaker_ind_central + thespeaker_sec_central + thespeaker_tech_central + thespeaker_tour_central + thespeaker_others_central
    south_total = thespeaker_agric_south + thespeaker_educ_south + thespeaker_health_south + thespeaker_ind_south + thespeaker_sec_south + thespeaker_tech_south + thespeaker_tour_south + thespeaker_others_south
    west_total = thespeaker_agric_west + thespeaker_educ_west + thespeaker_health_west + thespeaker_ind_west + thespeaker_sec_west + thespeaker_tech_west + thespeaker_tour_west + thespeaker_others_west

    cats = ["Agriculture", "Education", "Health", "Industry", "Security", "Technology", "Tourism", "Others"]
    thespeaker_the_totals = [thespeaker_agric_total, thespeaker_educ_total, thespeaker_health_total, thespeaker_ind_total, thespeaker_sec_total, thespeaker_tech_total, thespeaker_tour_total, thespeaker_others_total]

    regions_list = ["Northern", "Eastern", "Central", "Southern", "Western"]
    regions_totals = [north_total, east_total, central_total, south_total, west_total]
    
    north_total_list = [thespeaker_agric_north, thespeaker_educ_north, thespeaker_health_north, thespeaker_ind_north, thespeaker_sec_north, thespeaker_tech_north, thespeaker_tour_north, thespeaker_others_north]
    east_total_list = [thespeaker_agric_east, thespeaker_educ_east, thespeaker_health_east, thespeaker_ind_east, thespeaker_sec_east, thespeaker_tech_east, thespeaker_tour_east, thespeaker_others_east]
    central_total_list = [thespeaker_agric_central, thespeaker_educ_central, thespeaker_health_central, thespeaker_ind_central, thespeaker_sec_central, thespeaker_tech_central, thespeaker_tour_central, thespeaker_others_central]
    south_total_list = [thespeaker_agric_south, thespeaker_educ_south, thespeaker_health_south, thespeaker_ind_south, thespeaker_sec_south, thespeaker_tech_south, thespeaker_tour_south, thespeaker_others_south]
    west_total_list = [thespeaker_agric_west, thespeaker_educ_west, thespeaker_health_west, thespeaker_ind_west, thespeaker_sec_west, thespeaker_tech_west, thespeaker_tour_west, thespeaker_others_west]
    
    for r_item in regions_list:
        arr_regions_thespeaker.append(r_item)
    for r_total in regions_totals:
        arr_region_totals_thespeaker.append(r_total)
    for cat in cats:
        thespeaker_categories.append(cat)
    for total in thespeaker_the_totals:
        thespeaker_values.append(total)

    for n_total in north_total_list:
        n_total_values_thespeaker.append(n_total)
    for e_total in east_total_list:
        e_total_values_thespeaker.append(e_total)
    for c_total in central_total_list:
        c_total_values_thespeaker.append(c_total)
    for s_total in south_total_list:
        s_total_values_thespeaker.append(s_total)
    for w_total in west_total_list:
        w_total_values_thespeaker.append(w_total)

    # rendering all the stuff to the dashboard
    context_charts_view = {

        # *********** MP *****************

        # the 4 top cards
        'mp_cards_total': mp_cards_total,
        'mp_cards_solved': mp_cards_solved,
        'mp_cards_pending': mp_cards_pending,
        'mp_cards_inprogress': mp_cards_inprogress,
        'mp_cards_dataset': mp_cards_dataset,

        # the bar/column charts
        'mp_bar_categories': mp_bar_categories,
        'mp_bar_values': mp_bar_values,

        # piechart
        'mp_pie_categories': mp_pie_categories,
        'mp_pie_data': mp_pie_data,

        'mp_pie_total_agriculture': mp_pie_total_agriculture,
        'mp_pie_total_education': mp_pie_total_education,
        'mp_pie_total_health': mp_pie_total_health,
        'mp_pie_total_industry': mp_pie_total_industry,
        'mp_pie_total_security': mp_pie_total_security,
        'mp_pie_total_technology': mp_pie_total_technology,
        'mp_pie_total_tourism': mp_pie_total_tourism,
        'mp_pie_total_others': mp_pie_total_others,

        # 3D chart on the dashboard
        'mp_funnel_total_agriculture': mp_funnel_total_agriculture,
        'mp_funnel_total_education': mp_funnel_total_education,
        'mp_funnel_total_health': mp_funnel_total_health,
        'mp_funnel_total_industry': mp_funnel_total_industry,
        'mp_funnel_total_security': mp_funnel_total_security,
        'mp_funnel_total_technology': mp_funnel_total_technology,
        'mp_funnel_total_tourism': mp_funnel_total_tourism,
        'mp_funnel_total_others': mp_funnel_total_others,


        # ********************** THE SPEAKER **********************
        # the 4 top cards
        'total_subs_thespeaker': total_subs_thespeaker,
        'solved_thespeaker': solved_thespeaker,
        'pending_thespeaker': pending_thespeaker,
        'inprogress_thespeaker': inprogress_thespeaker,
        'dataset_thespeaker': dataset_thespeaker,

        # this is handling the bar/column/line charts
        'thespeaker_categories': thespeaker_categories, 
        'thespeaker_values': thespeaker_values,

        'thespeaker_agric_total': thespeaker_agric_total,
        'thespeaker_educ_total': thespeaker_educ_total,
        'thespeaker_health_total': thespeaker_health_total,
        'thespeaker_ind_total': thespeaker_ind_total,
        'thespeaker_sec_total': thespeaker_sec_total,
        'thespeaker_tech_total': thespeaker_tech_total,
        'thespeaker_tour_total': thespeaker_tour_total,
        'thespeaker_others_total': thespeaker_others_total,

        # this is for the global graph of cat and region vs the numbers
        'arr_regions_thespeaker': arr_regions_thespeaker,
        'arr_region_totals_thespeaker': arr_region_totals_thespeaker,
        'n_total_values_thespeaker': n_total_values_thespeaker,
        'e_total_values_thespeaker': e_total_values_thespeaker,
        'c_total_values_thespeaker': c_total_values_thespeaker,
        's_total_values_thespeaker': s_total_values_thespeaker,
        'w_total_values_thespeaker': w_total_values_thespeaker
    }

    return render(request, template_name, context_charts_view)     # Working # MP   # END MP


###############################################################################
#                  THE WEASYPRINT CLASSES ARE BELOW                           #
###############################################################################

# # we are creating a pdf off of the 'PdfResponseMixin' on the Submission details
# # Ref: https://spapas.github.io/2015/11/27/pdf-in-django/#id11
# class SubmisionsDetailPdfView(PdfResponseMixin, DetailView):
#     context_object_name = 'submission'
#     model = Submission


class SubmisionsDetailPdfView2(LoginRequiredMixin, ListView):
    template_name = 'stats/create_pdf_submission_details.html'

    def get_queryset(self):
        return Submission.objects.all()

    def get_context_data(self, *args, object_list=None, **kwargs):

        # Agriculture
        agric_north = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                                Q(region__icontains="Northern")).count()
        agric_east = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                               Q(region__icontains="Eastern")).count()
        agric_south = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                                Q(region__icontains="Southern")).count()
        agric_central = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                                  Q(region__icontains="Central")).count()
        agric_west = Submission.objects.filter(Q(submission_category__icontains="Agriculture") &
                                               Q(region__icontains="Western")).count()

        # Education
        educ_north = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                               Q(region__icontains="Northern")).count()
        educ_east = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                              Q(region__icontains="Eastern")).count()
        educ_south = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                               Q(region__icontains="Southern")).count()
        educ_central = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                                 Q(region__icontains="Central")).count()
        educ_west = Submission.objects.filter(Q(submission_category__icontains="Education") &
                                              Q(region__icontains="Western")).count()

        # Health
        health_north = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                 Q(region__icontains="Northern")).count()
        health_east = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                Q(region__icontains="Eastern")).count()
        health_south = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                 Q(region__icontains="Southern")).count()
        health_central = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                   Q(region__icontains="Central")).count()
        health_west = Submission.objects.filter(Q(submission_category__icontains="Health") &
                                                Q(region__icontains="Western")).count()

        # Industry
        ind_north = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                              Q(region__icontains="Northern")).count()
        ind_east = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                             Q(region__icontains="Eastern")).count()
        ind_south = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                              Q(region__icontains="Southern")).count()
        ind_central = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                                Q(region__icontains="Central")).count()
        ind_west = Submission.objects.filter(Q(submission_category__icontains="Industry") &
                                             Q(region__icontains="Western")).count()

        # Security
        sec_north = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                              Q(region__icontains="Northern")).count()
        sec_east = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                             Q(region__icontains="Eastern")).count()
        sec_south = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                              Q(region__icontains="Southern")).count()
        sec_central = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                                Q(region__icontains="Central")).count()
        sec_west = Submission.objects.filter(Q(submission_category__icontains="Security") &
                                             Q(region__icontains="Western")).count()

        # Technology
        tech_north = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                               Q(region__icontains="Northern")).count()
        tech_east = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                              Q(region__icontains="Eastern")).count()
        tech_south = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                               Q(region__icontains="Southern")).count()
        tech_central = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                                 Q(region__icontains="Central")).count()
        tech_west = Submission.objects.filter(Q(submission_category__icontains="Technology") &
                                              Q(region__icontains="Western")).count()

        # Tourism
        tour_north = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                               Q(region__icontains="Northern")).count()
        tour_east = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                              Q(region__icontains="Eastern")).count()
        tour_south = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                               Q(region__icontains="Southern")).count()
        tour_central = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                                 Q(region__icontains="Central")).count()
        tour_west = Submission.objects.filter(Q(submission_category__icontains="Tourism") &
                                              Q(region__icontains="Western")).count()

        # Others
        others_north = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                 Q(region__icontains="Northern")).count()
        others_east = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                Q(region__icontains="Eastern")).count()
        others_south = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                 Q(region__icontains="Southern")).count()
        others_central = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                   Q(region__icontains="Central")).count()
        others_west = Submission.objects.filter(Q(submission_category__icontains="Others") &
                                                Q(region__icontains="Western")).count()

        # Totals >> ROWS
        agric_total = agric_north + agric_east + agric_central + agric_south + agric_west
        educ_total = educ_north + educ_east + educ_central + educ_south + educ_west
        health_total = health_north + health_east + health_central + health_south + health_west
        ind_total = ind_north + ind_east + ind_central + ind_south + ind_west
        sec_total = sec_north + sec_east + sec_central + sec_south + sec_west
        tech_total = tech_north + tech_east + tech_central + tech_south + tech_west
        tour_total = tour_north + tour_east + tour_central + tour_south + tour_west
        others_total = others_north + others_east + others_central + others_south + others_west

        # Totals >> cols
        north_total = agric_north + educ_north + health_north + ind_north + sec_north + tech_north + tour_north + others_north
        east_total = agric_east + educ_east + health_east + ind_east + sec_east + tech_east + tour_east + others_east
        central_total = agric_central + educ_central + health_central + ind_central + sec_central + tech_central + tour_central + others_central
        south_total = agric_south + educ_south + health_south + ind_south + sec_south + tech_south + tour_south + others_south
        west_total = agric_west + educ_west + health_west + ind_west + sec_west + tech_west + tour_west + others_west

        total_subs_as_per_cats = agric_total + educ_total + health_total + ind_total + sec_total + tech_total + tour_total + others_total
        total_subs_as_per_regions = north_total + east_total + central_total + south_total + west_total


        today = timezone.now()
        # context = super(GeneralSubmissionCountForTableView, self).get_context_data(**kwargs)
        context = {
            # Agriculture
            'agric_north': agric_north,
            'agric_east': agric_east,
            'agric_south': agric_south,
            'agric_central': agric_central,
            'agric_west': agric_west,

            # Education
            'educ_north': educ_north,
            'educ_east': educ_east,
            'educ_south': educ_south,
            'educ_central': educ_central,
            'educ_west': educ_west,

            # Health
            'health_north': health_north,
            'health_east': health_east,
            'health_south': health_south,
            'health_central': health_central,
            'health_west': health_west,

            # Industry
            'ind_north': ind_north,
            'ind_east': ind_east,
            'ind_south': ind_south,
            'ind_central': ind_central,
            'ind_west': ind_west,

            # Security
            'sec_north': sec_north,
            'sec_east': sec_east,
            'sec_south': sec_south,
            'sec_central': sec_central,
            'sec_west': sec_west,

            # Technology
            'tech_north': tech_north,
            'tech_east': tech_east,
            'tech_south': tech_south,
            'tech_central': tech_central,
            'tech_west': tech_west,

            # Tourism
            'tour_north': tour_north,
            'tour_east': tour_east,
            'tour_south': tour_south,
            'tour_central': tour_central,
            'tour_west': tour_west,

            # Others
            'others_north': others_north,
            'others_east': others_east,
            'others_south': others_south,
            'others_central': others_central,
            'others_west': others_west,

            # TOTALS >>
            # rows
            "agric_total": agric_total,
            "educ_total": educ_total,
            "health_total": health_total,
            "ind_total": ind_total,
            "sec_total": sec_total,
            "tech_total": tech_total,
            "tour_total": tour_total,
            "others_total": others_total,

            # cols
            "north_total": north_total,
            "east_total": east_total,
            "central_total": central_total,
            "south_total": south_total,
            "west_total": west_total,

            'total_subs_as_per_cats': total_subs_as_per_cats,
            'total_subs_as_per_regions': total_subs_as_per_regions,

            'today': today,
        }
        return context   # end table tabs 1,2,3


# # below we are applying weasy-print ie the django version
class SubmissionView(DetailView):
    # vanilla Django DetailView
    model = Submission
    template_name = 'stats/create_pdf_submission_details.html'


class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    # customized response class to change the default URL fetcher

    def get_url_fetcher(self):
        # disable host and certificate check
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)


class SubmissionPrintView(WeasyTemplateResponseMixin, SubmissionView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATIC_ROOT + '/static/reports/wprint.css',
    ]

    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False   # Change this to 'True' to disable preview and do a straight download
    # custom response class to configure url-fetcher
    response_class = CustomWeasyTemplateResponse


class SubmissionDownloadView(SubmissionPrintView):
    # # suggested filename (is required for attachment/download!)
    # print(Submission.objects.filter(), "********+++++++++++++++++++")
    # pdf_filename = '{}.pdf'.format(Submission.submission)
    pdf_filename = 'submission-details'

    # generate a PNG image instead
    # content_type = settings.THUMBNAIL_EXTENSION
    # pdf_filename = '{}.pdf'.format(Submission.submission)

    # dynamically generate filename
    def get_pdf_filename(self):
        return self.pdf_filename + '-{at}.pdf'.format(at=timezone.now().strftime('%d%m%Y-%H%M%S'), )
