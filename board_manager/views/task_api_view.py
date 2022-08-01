from rest_framework import generics,status
from rest_framework.response import Response
from board_manager.models import Task
from board_manager.serializers import TaskSerializer

class TasksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TasksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class FilterListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self, request, *args, **kwargs):
        pass