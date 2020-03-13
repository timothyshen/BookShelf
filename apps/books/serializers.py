from rest_framework import serializers

from users.serializers import AuthorSerializer
from .models import Book, BookCategory, Chapter


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('id', 'category_name', 'category_code', "is_tab", 'add_time', 'total_number')


class ChapterSerializer(serializers.ModelSerializer):

    def get
    class Meta:
        model = Chapter
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    book_type = CategorySerializer(read_only=True)
    Chapter = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'book_name', 'book_type', 'Chapter')
