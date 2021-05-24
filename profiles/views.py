import sys
sys.path.append('..')  # Adding a higher directory to python modules path.
import submissions

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, reverse, render
from django.views.generic import TemplateView, ListView, View
# from django.contrib.auth import get_user_model
from django.contrib import messages

from django.db.models import Count, Q

from .models import MyUser, Profile
from .forms import EditProfileForm
from submissions.models import Submission

User = MyUser


class EditProfile(LoginRequiredMixin, TemplateView):
    template_name = "profiles/edit_profile.html"

    def get(self, request, *args, **kwargs):
        user = self.request.user.profile

        if "profile_form" not in kwargs:
            kwargs["profile_edit_form"] = EditProfileForm(instance=user)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user.profile
        slug = self.request.user.profile.slug
        profile_form = EditProfileForm(request.POST, request.FILES, instance=self.request.user.profile)

        if not profile_form.is_valid():
            messages.error(request, "There was a problem with the form. Please check the details.")
            profile_form = EditProfileForm(instance=self.request.user.profile)
            return super(EditProfile, self).get(request, profile_form=profile_form)

        # form fine. Time to save!
        profile = profile_form.save(commit=False)
        profile.user.profile = user
        profile.save()
        # messages.success(request, "Profile details saved!")
        return redirect(reverse('profiles:show_self_details', kwargs={'slug': slug}))


@login_required
def all_profiles_list(request):    # ALL
    profiles_list = Profile.objects.all()

    for p in profiles_list:
        submissions_count = Submission.objects.filter(profile=p).count()
        print(submissions_count, '*******************************')

        context = {
            'profiles_list': profiles_list,
            'submissions_count': submissions_count,
            }
        return render(request, "profiles/profiles_list.html", context)


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "profiles/show_self_details.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        # q = Profile.objects.filter(slug__iexact=slug)

        if slug:
            profile = get_object_or_404(Profile, slug=slug)
            user = profile.user
            kwargs['user'] = user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["user"] = user
        return super(ProfileDetailView, self).get(request, *args, **kwargs)
