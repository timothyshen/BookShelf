from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import *


# Create your views here.


class BookcaseViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = 'book_id'

    def perform_create(self, serializer):
        book_case = serializer.save()
        books = book_case.book
        books.fav_num += 1
        books.save()

    def perform_destroy(self, instance):
        books = instance.book
        books.fav_num -= 1
        books.save()
        instance.delete()

    def get_queryset(self):
        return Bookcase.objects.filter(user=self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'list':
            return BookDetailSerializer
        else:
            return BookcaseSerializer
