from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView)


# Create your views here.

class BookcaseViewSet(ListCreateAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    permission_classes = ""
    authentication_classes = ''
    lookup_field = 'book_id'

    def get_queryset(self):
        return Bookcase.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return BookDetailSerializer
        elif self.action == 'create':
            return BookSerializer

        return BookSerializer
