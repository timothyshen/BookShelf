# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '13/06/2020 19:17'

from rest_framework import serializers
from .models import *
from books.serializers import BookSerializer, Book


class BookForIndexSerializer(serializers.ModelSerializer):
    book_author = serializers.PrimaryKeyRelatedField(read_only=True, source='book_author.username')

    class Meta:
        model = Book
        fields = ('id', 'book_author', 'book_image', 'book_name', 'book_short_description')


class IndexPageSerializer(serializers.ModelSerializer):
    book = BookForIndexSerializer(read_only=True)

    class Meta:
        model = IndexPage
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class IndexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexImage
        fields = '__all__'


class CategoryImageSerializer(serializers.ModelSerializer):
    book = BookForIndexSerializer(read_only=True)

    class Meta:
        model = CategoryImagePage
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(CategoryImageSerializer, self).to_representation(instance)
        rep['type'] = instance.type.type_name
        return rep



class CategoryPageSerializer(serializers.ModelSerializer):
    book = BookForIndexSerializer(read_only=True)

    class Meta:
        model = CategoryPage
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(CategoryPageSerializer, self).to_representation(instance)
        rep['type'] = instance.type.type_name
        return rep
