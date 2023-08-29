from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", TaskListView, name="task-list"),
    path("create/", TaskCreateView, name="task-create"),
    path("update/<int:task_id>/", TaskUpdateView, name="task-update"),
    path("delete/<int:task_id>/", TaskDeleteView, name="task-delete"),
]
