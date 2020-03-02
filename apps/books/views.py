from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView)
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from .serializers import *


# Create your views here.

class BookCreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterCreate(ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class BookCategoryDetailView(ListCreateAPIView, RetrieveModelMixin):
    queryset = BookCategory.objects.all()
    serializer_class = CategorySerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

