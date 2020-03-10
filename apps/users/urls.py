from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()

urlpatterns = [
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("user/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
    path("user", UserCreate.as_view(), name='user'),
    path("profile/reader/<int:pk>", ReaderProfileDetailView.as_view(), name="reader"),
    path("profile/author/<int:pk>", AuthorProfileDetailView.as_view(), name="reader"),
    path(r'login/', obtain_jwt_token)
]
