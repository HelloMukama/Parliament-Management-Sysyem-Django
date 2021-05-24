from django.urls import path, re_path

from .reports import create_pdf_report_main_table
from .views import (
    GeneralSubmissionCountForTableView,

    # dashboard
    render_all_data_to_dash,

    # statistics page
    render_all_data_for_mp_charts_view, 
   
    # create_pdf_report_main_table,
    # SubmisionsDetailPdfView,
    SubmisionsDetailPdfView2,
    SubmissionDownloadView, 
    # create_pdf_submission_details2
    )


app_name = "stats"

urlpatterns = [
    # /...

    # dashboard
    path('dashboard/', render_all_data_to_dash, name='dashboard'),

    # statistics
    path('stats/cat-nums/', GeneralSubmissionCountForTableView.as_view(), name="submissions_cat_n_region_count"),

    # charts view
    path('charts-view/', render_all_data_for_mp_charts_view, name="charts_view"),
]


""" REPORTS """
urlpatterns += [
    # path('submissions/report', include('model_report.urls')),
    path('submissions/create-pdf-main-table/', create_pdf_report_main_table, name='create_pdf_report_main_table'),
    
    # re_path('^submissions/submission-(?P<pk>[0-9]+)/details/pdf/$', SubmisionsDetailPdfView.as_view(),
    # name='create_pdf_submission_details'),

    # re_path('^submissions/submission-(?P<pk>[0-9]+)/details/pdf/$', SubmisionsDetailPdfView2.as_view(),
    # name='create_pdf_submission_details'),

    re_path('^submissions/submission-(?P<pk>[0-9]+)/details/pdf/$', SubmissionDownloadView.as_view(), name='create_pdf_submission_details'),
    # # re_path('^submissions/submission-(?P<pk>[0-9]+)/details/pdf/$', create_pdf_submission_details2, name='create_pdf_submission_details'),

]
