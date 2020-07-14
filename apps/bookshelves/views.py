from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import *
from books.models import Chapter


# Create your views here.


class BookcaseViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    lookup_field = 'book_id'

    def get_queryset(self):
        return Bookcase.objects.filter(user=self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'list':
            return BookCaseDetailSerializer
        else:
            return BookCaseSerializer


class BookMarkViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return BookMark.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return BookMarkDetailSerializer
        else:
            return BookMarkSerializer



    def perform_create(self, serializer):
        return serializer.save()
