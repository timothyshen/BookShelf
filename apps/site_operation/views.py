from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class IndexPageView(ModelViewSet):
    serializer_class = IndexPageSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return IndexPage.objects.filter(activation='Active')


class IndexImageView(ModelViewSet):
    serializer_class = IndexImageSerializer
    queryset = IndexImage.objects.all()
