from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from .serializers import *

User = get_user_model()


class UserCreate(ListCreateAPIView):
    """
    User fetch and creation
    list:
        get all users
    create:
        create new users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def update(self, request, *args, **kwargs):
        try:
            partial = True
            instance = self.get_object()
            instance.id = kwargs.get('pk')
            serializer = self.get_serializer(instance=instance, data=request.data, partial=partial)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return Response({"status": True}, status=status.HTTP_201_CREATED)
        except ValidationError as err:
            return Response({"status": False, "error_description": err.detail}, status=status.HTTP_400_BAD_REQUEST)
