from rest_framework import serializers
from users.serializers import UserDetailSerializer
from .models import Book, BookCategory, Chapter
from .filters import CustomerHyperlink


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('id', 'category_name', 'category_code', "is_tab", 'add_time', 'total_number')


class ChapterSerializer(serializers.ModelSerializer):
    # url = CustomerHyperlink(
    #     many=True,
    # )

    class Meta:
        model = Chapter
        # fields = ('chapter_title','url',)
        fields = '__all__'


class ChapterDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = CustomerHyperlink(
        view_name='chapter-detail'
    )

    class Meta:
        model = Chapter
        fields = ('url','id','chapter_title','book')


class BookSerializer(serializers.ModelSerializer):
    book_type = CategorySerializer(read_only=True)
    chapter = ChapterDetailSerializer(many=True, read_only=True)
    book_author = serializers.PrimaryKeyRelatedField(read_only=True, source='book_author.username')

    class Meta:
        model = Book
        fields = '__all__'

