from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('add/', views.add_task, name='add_task'),
    path('task/<int:task_id>/toggle/', views.toggle_task_status, name='toggle_task_status'),
    path('task/<int:task_id>/', views.delete_task, name = 'delete_task'),
    path('delete_all/', views.delete_all_task, name = 'delete_all_task'),
]