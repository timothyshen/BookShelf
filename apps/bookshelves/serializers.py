from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from books.serializers import BookSerializer, ChapterDetailSerializer
from .models import Bookcase, BookMark  #


class BookMarkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = BookMark
        fields = '__all__'

    def create(self, validated_data):
        print('hi')
        chapter_id_val = validated_data.pop('chapter')
        user_id_val = validated_data.pop('user')
        exist_book = Bookcase.objects.get(book__pk=chapter_id_val.book_id, user__pk=user_id_val.id)
        print(exist_book.bookmark.id)
        if exist_book:
            exist_bookmark = exist_book.bookmark.id

            if exist_bookmark:
                print(exist_bookmark)
                print(user_id_val.id)
                bookmark = BookMark.objects.filter(id=exist_bookmark).update(chapter_id=chapter_id_val.id,
                                                                          **validated_data)
                print('exist_bookmark update')
                print(bookmark)
            else:
                bookmark = BookMark.objects.create(user_id=user_id_val.id, chapter_id=chapter_id_val.id,
                                                   **validated_data)
                Bookcase.objects.filter(book__chapter=chapter_id_val.id, user_id=user_id_val.id).update(bookmark_id=bookmark.id)
                print('bookmark create')
                print(bookmark)
        else:
            bookmark = BookMark.objects.create(user_id=user_id_val.id, chapter_id=chapter_id_val.id, **validated_data)
            print(bookmark)
            Bookcase.objects.create(user_id=user_id_val.id, book_id=chapter_id_val.book_id, bookmark_id=bookmark.id)

        return bookmark


class BookMarkDetailSerializer(serializers.ModelSerializer):
    chapter = ChapterDetailSerializer()
    class Meta:
        model = BookMark
        fields = '__all__'


class BookCaseDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    bookmark = BookMarkDetailSerializer()

    class Meta:
        model = Bookcase
        fields = ('user', 'book', 'id', 'bookmark')


class BookCaseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Bookcase
        validators = [
            UniqueTogetherValidator(
                queryset=Bookcase.objects.all(),
                fields=('user', 'book'),
                message='Already existing in the bookcase'
            )
        ]

        fields = ('id', 'user', 'book', 'bookmark')
