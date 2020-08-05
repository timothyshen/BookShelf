from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book
User = get_user_model()
# Create your models here.

class UserComment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book', related_name='book_comment')
    message = models.TextField(default='', verbose_name='Content')
    like_num = models.IntegerField(default=0, verbose_name='Liked_vote', editable=False)
    sub_comment = models.ForeignKey("self", null=True, blank=True, verbose_name="Parent message", help_text="parent index",
                                        related_name="reply_message", on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Added time")

    class Meta:
        verbose_name = "User comment"
        verbose_name_plural = verbose_name

