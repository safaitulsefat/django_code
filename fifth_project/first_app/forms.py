from typing import Any
from django import forms
from django.core import validators

class contact_form(forms.Form):
    name = forms.CharField(label='user name',initial='sefat',help_text='must be 70 character')
    file = forms.FileField()
    email = forms.EmailField(label='email')
    age=forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICE = [('s','small'),('m','medium'),('b','big')]
    size = forms.ChoiceField(choices=CHOICE)
    multi = [('c','cheese'),('i','italin')]
    pizza = forms.MultipleChoiceField(choices=multi,widget=forms.CheckboxSelectMultiple)
    
# class student(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
#     '''def clean_name(self):
#         valname = self.cleaned_data['name']
#         if len(valname) < 10:
#             raise  forms.ValidationError("enter a name which at list 10 chacter")
#         return valname
#     def clean_email(self):
#         valemail = self.cleaned_data['email']
#         if '.com' not in valemail:
#             raise forms.ValidationError("use .com")
#         return valemail
#             '''
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise  forms.ValidationError("enter a name which at list 10 chacter")
       
    
#         if '.com' not in valemail:
#             raise forms.ValidationError("use .com")

def check_length(value):
    if len(value) < 10:
        raise forms.ValidationError('enter at least 10')
class student(forms.Form):
     name = forms.CharField(validators=[validators.MinLengthValidator(10,message='enter a name with at least 10 character')])
     text = forms.CharField(validators=[check_length])
     email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='enter email')])
     age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message='enter under 34'),validators.MinValueValidator(24,message='enter 24 above')])
     file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['png'],message='file extension must be png')])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data['name']
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['confirm']
        if len(password) <6 and len(confirm) <6:
            raise forms.ValidationError('enter at least 6') 
        if password != confirm:
            raise forms.ValidationError('password doesnot match')
        if len(name)<10:
            raise forms.ValidationError('please enter at least 10 chracter')