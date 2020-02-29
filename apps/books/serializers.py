from rest_framework import serializers
from .models import Book, BookCategory, Chapter
from users.serializers import AuthorSerializer


class CategorySerializer2(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many = True)

    class Meta:
        model = BookCategory
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields='__all__'


class BookSerializer(serializers.ModelSerializer):
    book_author = AuthorSerializer()
    chapter = ChapterSerializer()
    class Meta:
        model = Book
        fields = '__all__'

