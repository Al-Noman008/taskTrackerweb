
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class=TaskSerializer
    queryset=Task.objects.all()
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer