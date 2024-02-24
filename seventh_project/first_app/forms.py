from django import forms
from . import models
class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        labels={
            'name':'student name',
            'roll':'student roll'
        }
        
        widgets={
            'name':forms.TextInput(),
            
        }
        error_messages = {
            'name':{'required':'your name is required'}
        }
        