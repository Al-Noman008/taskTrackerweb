from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TaskList.as_view(), name='task'),
    path('task/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
]