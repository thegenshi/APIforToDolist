from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ToDo, SignUp


class ToDoSerializer(ModelSerializer):
      class Meta:
        model = ToDo
        fields = ('title', 'description', 'create_at', 'is_complete')

class SignUpSerializer(ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    class Meta:
      model = SignUp
      fields = ('first_name', 'last_name', 'username', 'email', 'password')