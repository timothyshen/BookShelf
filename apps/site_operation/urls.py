#_*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '13/06/2020 19:45'

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'index_link', IndexPageView, base_name='indexLink')
router.register(r'index_image', IndexImageView, base_name='indexImage')


urlpatterns = [
    path('category_page/<type>', CategoryPageView.as_view(), name='category-page-detail'),
    path('category_image/<type>', CategoryImageView.as_view(), name='category-image-detail'),

]
urlpatterns += router.urls
