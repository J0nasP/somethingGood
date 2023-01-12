from django.db import models

class TodoItem(models.Model):
    todoId = models.CharField(max_length=100, primary_key=True),
    label = models.CharField(max_length=100),
    done = models.BooleanField(default=False)



