from django.test import TestCase
# from django.core.urlresolvers import resolve, reverse
from django.urls import reverse, resolve
# from django.contrib.auth import get_user_model

from django.conf import settings as project_settings
User = project_settings.AUTH_USER_MODEL


class PageOpenTestCase(TestCase):
    def test_home_page_exists(self):
        url = reverse('home')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_about_page_exists(self):
        url = reverse('about')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)


class ProfileTestCase(TestCase):
    def test_profiles_created(self):
        u = User.objects.create_user(email="dummy@example.com")
        self.assertIsNotNone(u.profile)
