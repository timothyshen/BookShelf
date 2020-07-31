from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *



# Create your views here.

class IndexPageView(ModelViewSet):
    serializer_class = IndexPageSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return IndexPage.objects.filter(activation='Active')


class IndexImageView(ModelViewSet):
    serializer_class = IndexImageSerializer
    queryset = IndexImage.objects.all()


class CategoryPageView(ListAPIView):
    serializer_class = CategoryPageSerializer

    def get_queryset(self):
        return CategoryPage.objects.filter(type__type_name=self.kwargs.get('type', None), activation='Active')

class CategoryImageView(ListAPIView):
    serializer_class = CategoryImageSerializer

    def get_queryset(self):
        return CategoryImagePage.objects.filter(type__type_name=self.kwargs.get('type', None), activation='Active')
