from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    # # FOR THE ADMIN, WE ARE GOING TO REDIRECT UNAUTHORISED ACCESS TO A FAKE ADMIN PAGE
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('2021secret1408/', admin.site.urls),

    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('', include('index.urls')),
    path('about/', include('about.urls')),
    path('account/', include('accounts.urls')),
    
    path('settings/system/', include('personalsettings.urls')),
    path('user/', include('profiles.urls')),
    path('submissions/', include('submissions.urls')),
    path('', include('stats.urls')),


    path('submissions/comments/', include('comment.urls')),
    # path('api/', include('comment.api.urls')),  # only required for API Framework

]

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# # lines below disable the new django admin navbar that is shipped with django3.*
# admin.autodiscover()
# admin.site.enable_nav_sidebar = False
