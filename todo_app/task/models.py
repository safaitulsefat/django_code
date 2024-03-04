from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTitle=models.CharField(max_length=20)
    taskDescription=models.CharField(max_length=20)
    is_completed=models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    def __str__(self) -> str:
        return f"{self.taskTitle}"