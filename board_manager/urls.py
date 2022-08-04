from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from board_manager.views import TasksListCreateAPIView, TasksRetrieveUpdateDestroyAPIView

urlpatterns = format_suffix_patterns([
    path(
        "tasks/",
        TasksListCreateAPIView.as_view(),
        name='tasks'
    ),
    path(
        "tasks/<int:pk>/",
        TasksRetrieveUpdateDestroyAPIView.as_view(),
        name='task'
    )
])