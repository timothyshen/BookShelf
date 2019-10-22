# Create your tests here.
from django.test import TestCase
import unittest
from .models import User


class test_module(TestCase):
    def setUp(self):
        User.objects.create()
