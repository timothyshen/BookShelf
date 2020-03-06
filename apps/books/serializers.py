from rest_framework import serializers

from users.serializers import AuthorSerializer
from .models import Book, BookCategory, Chapter


class CategorySerializer(serializers.ModelSerializer):
    total_number = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = BookCategory
        fields = ('id','category_name', 'category_code', "is_tab", 'add_time', 'total_number')

    def get_total_number(self, obj):
        return Book.objects.annotate(book_type="category_name")

class BookSerializer(serializers.ModelSerializer):
    book_type = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    # book_id = BookSerializer()

    class Meta:
        model = Chapter
        fields = '__all__'
