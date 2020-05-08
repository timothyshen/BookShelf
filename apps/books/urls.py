from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()


urlpatterns = [
    path('book/', include([
        path('all-category', BookCategoryDetailView.as_view(), name='all-category'),
        path('detail', BookList.as_view(), name='chapter_create'),
        path('detail/<int:pk>', BookDetailView.as_view(), name='chapter_create'),
        path('chpater/<int:book_id>/<int:pk>', ChapterDetailView.as_view(), name='chapter_change')
    ])),
]
