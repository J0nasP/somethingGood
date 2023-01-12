from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    todoId = models.CharField(max_length=100, blank=False, null=False, primary_key=True),
    label = models.CharField(max_length=100, blank=False, null=False),
    done = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.label
