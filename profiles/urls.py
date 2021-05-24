from django.urls import path

from .views import ( 
	ProfileDetailView, 
	EditProfile, 
	all_profiles_list
	)

app_name = 'profiles'

urlpatterns = [
    # /user/...
    path('list/', all_profiles_list, name='profiles_list'),

    path('<slug>/', ProfileDetailView.as_view(), name='show_self_details'),

    path('<slug>/edit/', EditProfile.as_view(), name='edit_self'),
]
