from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()


urlpatterns = [
    path('book/', include([
        path('all-category', BookCategoryDetailView.as_view(), name='all-category'),
        path('list', BookCreate.as_view(), name='book'),
        path('list/<int:pk>', BookDetailView.as_view(), name='book_detail'),
        path('list/chapter/create/<book_id>/', ChapterCreate.as_view(), name='chapter_create'),
        path('list/chapter/edit/<int:pk.book.id>/<int:pk>', ChapterDetailView.as_view(), name='chapter_change')
    ])),
]
