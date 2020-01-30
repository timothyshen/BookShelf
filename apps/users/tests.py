# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase


class TestProfileModel(TestCase):
    def test_profile_creation(self):
        test_user = get_user_model()
        user = test_user.objects.create(username='n.shi', password='1239Shen')
        print('true')
        user.save()
