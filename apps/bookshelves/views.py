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
            return BookCaseDetailSerializer
        else:
            return BookCaseSerializer


class BookMarkViewSet(ModelViewSet):
    serializer_class = BookMarkSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return BookMark.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        book_id_var = request.query_params['book_id']
        bookcase_id_var = request.query_params['bookcase_id']
        instance = self.get_object()
        try:
            exist_book = Bookcase.objects.get(id=bookcase_id_var, book_id=book_id_var)
            if exist_book:
                exist_chapter = Chapter.objects.get(book_id=book_id_var, id=instance.chapter.id)
                if exist_chapter:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    return Response({"status": True}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = self.get_object()
                instance.id = kwargs.get('pk')
                serializer = self.get_serializer(instance=instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response({"status": True}, status=status.HTTP_201_CREATED)
        except ValidationError as err:
            return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        return serializer.save()
