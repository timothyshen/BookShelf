# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import Reader


# Create your views here.
def index(request):
    return render(request, 'index.html')


class UsersListView(APIView):
    def get(self, request, format=None):
        users = Reader.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)
