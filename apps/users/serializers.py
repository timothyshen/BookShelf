from rest_framework import serializers
from .models import Reader


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'
