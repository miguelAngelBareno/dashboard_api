from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from board_manager.models import Task
from board_manager.serializers import TaskSerializer

class TasksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task_name','state','priority']

class TasksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer