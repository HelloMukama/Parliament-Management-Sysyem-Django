from django.urls import path, include

from .views import IndexTemplateView, UserGuideView

app_name = "index"

urlpatterns = [
    # 127.0.0.1/...
    # path('', IndexTemplateView.as_view(), name="site_index"),

    # the user guide instructions
    path('help/', UserGuideView.as_view(), name="user_guide"),
]


"""
NB.  the index site was coliding with the login side because we are sendind 2 pages to 1 url
So, this index is active as in the template but not the url

Also, the 2 urls can stay active or have the index one off.
the login one cannot go off as it would disappear the login form

then in case of anything to be added to the index page, the index html file is working
as is the login file

"""



#  The error pageurls
handler400 = 'index.views.bad_request_400_view'
handler403 = 'index.views.permission_denied_403_view'
handler404 = 'index.views.page_not_found_404_view'
handler500 = 'index.views.error_500_view'