from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()



urlpatterns = [
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
    path('user', userCreate.as_view(), name='user')
]
