from rest_framework import serializers

from books.serializers import BookSerializer
from .models import  Bookcase

class BookDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Bookcase
        fields =('book', 'id')

class BookSerializer(serializers.Serializer)