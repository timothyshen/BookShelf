from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (ListCreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import *
from .serializers import *


# Create your views here.

# for home page


class UserMessageForBook(ListCreateAPIView):

    def get_queryset(self):
        queryset1 = UserComment.objects.filter(book_id=self.kwargs.get('book_id', None))

        return queryset1

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserMessage
        elif self.request.method == 'GET':
            return UserMessageList

    def get_authenticators(self):
        if self.request.method == 'POST':
            return [JSONWebTokenAuthentication(), SessionAuthentication()]


class UserMessageForUser(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserMessage

    def get_queryset(self):
        return UserComment.objects.filter(user=self.request.user)


class UserMessageEditForUser(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserMessage

    def get_queryset(self):
        return UserComment.objects.filter(user=self.request.user)


class BookCommentList(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserMessageForAuthor

    def get_queryset(self):
        return UserComment.objects.filter(book_id=self.kwargs.get('book_id', None))
