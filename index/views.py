from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class IndexTemplateView(TemplateView):
    template_name = "index/site_index.html"


class UserGuideView(LoginRequiredMixin, TemplateView):
    template_name = "index/user_guide.html"



# ERROR views
def page_not_found_404_view(request, exception):
    return render(request, "index/404.html", {})


def error_500_view(request, exception=None):
    return render(request, "index/500.html", {})


def permission_denied_403_view(request, exception=None):
    return render(request, "index/403.html", {})


def bad_request_400_view(request, exception=None):
    return render(request, "index/400.html", {})
