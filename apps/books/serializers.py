from rest_framework import serializers
from .models import Book, BookCategory


class CategorySerializer2(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many = True)

    class Meta:
        model = BookCategory
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
