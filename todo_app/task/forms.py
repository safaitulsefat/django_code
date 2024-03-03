from django import forms
from task.models import TaskModel
class taskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDescription','is_completed']