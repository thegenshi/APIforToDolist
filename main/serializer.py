from rest_framework.serializers import ModelSerializer
from .models import ToDo


class ToDoSerializer(ModelSerializer):
      class Meta:
        model = ToDo
        fields = ('title', 'description', 'create_at', 'is_complete')