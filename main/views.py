from django.shortcuts import render
from .models import ToDo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializer import ToDoSerializer

# Create your views here.

class ToDoListView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoCreateView(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoUpdateView(generics.UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDestroyView(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)