from . import views
from django.urls import path


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add-task/', views.add_task, name='add_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]
