from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    return HttpResponse('''
                        <h1>this is about page</h1>
                        <a href='/first_app/contact'>contact</a>
                        <a href='/second_app/course'>course</a>
                        <a href='/second_app/feedback'>feedback</a>
                        ''')
def contact(request):
    return HttpResponse('''
                        <h1>this is contact page</h1>
                        <a href='/second_app/course'>course</a>
                        <a href='/first_app/about'>about</a>
                        <a href='/second_app/feedback'>feedback</a>
                        ''')