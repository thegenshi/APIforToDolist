from django.shortcuts import render
from .models import ToDo, SignUp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializer import ToDoSerializer, SignUpSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ToDoListView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = IsAuthenticated

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

class SignUpView(generics.CreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer