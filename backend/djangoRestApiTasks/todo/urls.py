from django.urls import path
from todo import views

urlpatterns = [
    path('todos/', views.tasks),
    path('todos/<int_pk>', views.task_details)
]