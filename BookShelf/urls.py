"""BookShelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from BookShelf.settings import MEDIA_ROOT
from books.views import AuthorBookViewSet, AuthorChapterViewSet
from bookshelves.views import BookcaseViewSet, BookMarkViewSet

router = DefaultRouter()
#
router.register(r'bookcase', BookcaseViewSet, base_name='bookcase')
router.register(r'bookmark', BookMarkViewSet, base_name='bookmark')
router.register(r'create', AuthorBookViewSet, base_name='create_book')
router.register(r'create/(?P<book_id>[^/.]+)/chapter', AuthorChapterViewSet, base_name='create_chapter')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # token
    path('api-token-auth/', views.obtain_auth_token),
    path(r'',
         TemplateView.as_view(template_name="index.html"),
         name='app', ),
    path(r'', include(router.urls)),
    path('docs/', include_docs_urls(title='User')),
    path('', include('users.urls')),
    path('', include('books.urls')),
    path('', include('site_operation.urls')),
    path('', include('user_operation.urls'))

]
