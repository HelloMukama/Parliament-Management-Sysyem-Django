import sys
sys.path.append('..')  # Adding a higher directory to python modules path.
import submissions
from submissions.models import Submission

from django.http import HttpResponse
from django.db.models import Count, Q
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.text import slugify

from django.utils import timezone


# This is creating a report for the main table that we have in the statistics page
def create_pdf_report_main_table(request):
    template_path = 'stats/create_pdf_report_main_table.html'
    subs = Submission.objects.all()

    today = timezone.now()

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
    tour_total = tech_north + tour_east + tour_central + tour_south + tour_west
    others_total = others_north + others_east + others_central + others_south + others_west

    # Totals >> cols
    north_total = agric_north + educ_north + health_north + ind_north + sec_north + tech_north + tour_north + others_north
    east_total = agric_east + educ_east + health_east + ind_east + sec_east + tech_east + tour_east + others_east
    central_total = agric_central + educ_central + health_central + ind_central + sec_central + tech_central + tour_central + others_central
    south_total = agric_south + educ_south + health_south + ind_south + sec_south + tech_south + tour_south + others_south
    west_total = agric_west + educ_west + health_west + ind_west + sec_west + tech_west + tour_west + others_west

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

        'today': today,
        'subs': subs,
        'request': request
    }

    # Create a django-specific object and specify the context type as pdf
    response = HttpResponse(content_type='application/pdf')

    # # 'attachment below downloads the pdf
    # response['Content-Disposition'] = 'attachment; filename="general_table.pdf"'

    # Removing it leaves it as a preview format pdf
    response['Content-Disposition'] = "filename=general_table.pdf"

    # find the template and render it
    template = get_template(template_path)
    html = template.render(context)

    # create pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    # if error, show sth
    if pisa_status.err:
        return HttpResponse("Error <pre>" + html + " !!!!</pre>")
    return response


# from model_report.report import reports, ReportAdmin
#
#
# class SubmissionReport(ReportAdmin):
#     title = _('The report on submission abc...')
#     model = Submission
#     fields = [
#         'user',
#         'district',
#         'region',
#         'submission',
#         'description',
#         'timestamp',
#     ]
#     list_order_by = ('-timestamp',)
#     type = 'report'
#
#
# reports.register('Submission-report', SubmissionReport)
