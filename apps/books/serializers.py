from rest_framework import serializers

from users.serializers import AuthorSerializer
from .models import Book, BookCategory, Chapter


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"








class BookSerializer(serializers.ModelSerializer):
    book_author = AuthorSerializer()
    book_type = CategorySerializer()

    class Meta:
        model = Book
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    # book_id = BookSerializer()

    class Meta:
        model = Chapter
        fields = '__all__'