#_*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '04/08/2020 20:03'
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('comment/<book_id>', UserMessageForBook.as_view(), name='comment-detail'),
    path('comment/user/', UserMessageForUser.as_view(), name='user-comment-detail'),
    path('comment/user/<int:pk>', UserMessageEditForUser.as_view(), name='user-comment-change'),
    path('comment/book/<book_id>', BookCommentList.as_view(), name='book-comment-detail')
]
