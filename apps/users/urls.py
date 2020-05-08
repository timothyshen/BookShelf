from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
router = DefaultRouter()

urlpatterns = [
    # retrieves profile details of the currently logged in user
    path("user/<int:pk>", UserDetailView.as_view(), name="profile"),
    path("user", UserCreate.as_view(), name='user'),
    path(r'api/token/', obtain_jwt_token),
    path(r'api/token/update/', refresh_jwt_token)
]
