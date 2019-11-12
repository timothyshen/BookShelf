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
from rest_framework.documentation import include_docs_urls

from users.views import UsersListView
from BookShelf.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'', TemplateView.as_view(template_name="application.html")),
    path('docs', include_docs_urls(title='User')),
    path('users/', UsersListView.as_view(), name='users-list'),
    # path('login/', LoginView.as_view(), name='login')
    #     path('bookcase/'. BookListView.as_view(), name='users-list')
]
