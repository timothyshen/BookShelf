from django.db.models import F
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView,
                                     RetrieveAPIView)
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from django.db.models import Count
from rest_framework.decorators import action
from utils.permissions import IsAuthorPermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import *


# Create your views here.


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterCreate(ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class BookCategoryDetailView(ListCreateAPIView, RetrieveModelMixin):
    queryset = BookCategory.objects.all()
    serializer_class = CategorySerializer


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Book.objects.filter(pk=instance.id).update(total_click=F('total_click') + 1)
        chapter_count = Chapter.objects.filter(book=instance.id).count()
        Book.objects.filter(pk=instance.id).update(chapter_count=chapter_count)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ChapterDetailView(RetrieveAPIView):
    serializer_class = ChapterSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        return Chapter.objects.filter(book=self.kwargs.get('book_id', None)).all()




class AuthorBookViewSet(ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = BookSerializer
    # permission_classes = (IsAuthorPermission,)

    def perform_create(self, serializer):
        return serializer.save(book_author=self.request.user)

    def get_queryset(self):
        return Book.objects.filter(book_author=self.request.user)


class AuthorChapterViewSet(ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ChapterSerializer
    permission_classes = IsAuthorPermission
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def perform_create(self, serializer):
        chapter = serializer.save()

    def get_queryset(self):
        return Chapter.objects.filter(book__book_author=self.request.user)
