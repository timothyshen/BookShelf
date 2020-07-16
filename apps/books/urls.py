from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()


urlpatterns = [
    path('book/', include([
        path('all-category', BookCategoryDetailView.as_view(), name='all-category'),
        path('detail', BookList.as_view(), name='book-list'),
        path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
        path('chapter/<book_id>/<chapter_id>', ChapterDetailView.as_view(),name='chapter-detail'),
        path('<request_item>', TopBookValueViewSet.as_view(), name='ranking-detail'),
        path('<requestCategory>/<request_item>', TopBookByCategory.as_view(), name='category-ranking-detail')

    ])),
]
