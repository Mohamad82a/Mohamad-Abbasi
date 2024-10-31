from django.urls import path
from .views import task_list, task_details

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('tasks/<int:id>/', task_details, name='task-detail'),
]
