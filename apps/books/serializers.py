from rest_framework import serializers
from .models import Book, BookCategory

class CategorySerializer2(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer)：
    su

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'
