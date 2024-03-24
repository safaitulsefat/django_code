from django import forms
from task.models import TaskModel
class taskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDescription','priority','due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }