# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '13/06/2020 19:17'

from rest_framework import serializers
from .models import *
from books.serializers import BookSerializer, Book

class BookForIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=('id', 'book_name', 'book_short_description')


class IndexPageSerializer(serializers.ModelSerializer):
    book = BookForIndexSerializer(read_only=True)


    class Meta:
        model = IndexPage
        fields = '__all__'



class IndexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexImage
        fields = '__all__'
