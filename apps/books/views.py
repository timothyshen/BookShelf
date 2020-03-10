from django.db.models import F
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView)
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


# Create your views here.

class BookCreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def create(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     bookType = instance.book_type
    #     BookCategory.objects.filter(category_name__contains= bookType).update(total_number= F('total_number') + 1)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

class ChapterCreate(ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class BookCategoryDetailView(ListCreateAPIView, RetrieveModelMixin):
    queryset = BookCategory.objects.all()
    serializer_class = CategorySerializer



class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Book.objects.filter(pk=instance.id).update(total_click=F('total_click') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ChapterDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

