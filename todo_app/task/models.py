from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTitle=models.CharField(max_length=20)
    taskDescription=models.CharField(max_length=20)
    is_completed=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    priority = models.IntegerField(choices=[(i, str(i)) for i in range(9)])
    due_date = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.taskTitle}"