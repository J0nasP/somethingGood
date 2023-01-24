from django.db import models

# Create your models here.

class TodoTask(models.Model):
    taskId = models.AutoField(primary_key=True,)
    label = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.label