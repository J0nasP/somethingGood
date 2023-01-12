from django.urls import path
from todo import views

urlpatterns = [
    path('todos/', views.todo_items),
    path('todos/<int_pk>', views.todo_items_details)
]