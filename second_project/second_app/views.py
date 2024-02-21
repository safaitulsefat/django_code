from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def course(request):
    return HttpResponse('''
                        <h1>this is couse page</h1>
                        <a href='/first_app/contact'>contact</a>
                        <a href='/first_app/about'>about</a>
                        <a href='/second_app/feedback'>feedback</a>
                        ''')
def feedback(request):
    return HttpResponse('''
                        <h1>this is feedback page</h1>
                        <a href='/first_app/contact'>contact</a>
                        <a href='/first_app/about'>about</a>
                        <a href='/second_app/course'>cours</a>
                        ''')