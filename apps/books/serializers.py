from rest_framework import serializers
from .models import Book, BookCategory, Chapter
from .filters import CustomerHyperlink


class CategorySerializer(serializers.ModelSerializer):
    total_number = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookCategory
        fields = ('id', 'category_name', 'category_code', "is_tab", 'add_time', 'total_number')


class ChapterSerializer(serializers.ModelSerializer):
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
        fields = ('url', 'id', 'chapter_title', 'book')


class BookSerializer(serializers.ModelSerializer):
    chapter = ChapterDetailSerializer(many=True, read_only=True)
    book_author = serializers.PrimaryKeyRelatedField(read_only=True, source='book_author.username')
    chapter_count = serializers.IntegerField(read_only=True)
    total_words = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ('id','book_name', 'book_image', 'book_status', 'book_author', 'book_type', 'book_short_description',
                  'book_description', 'chapter','total_words', 'chapter_count', 'total_vote', 'total_click',
                  'fav_num', 'added_time', 'last_update')

    def to_representation(self, instance):
        rep = super(BookSerializer, self).to_representation(instance)
        rep['book_type'] = instance.book_type.category_name
        return rep
