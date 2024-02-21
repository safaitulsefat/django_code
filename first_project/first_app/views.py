from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("sefat")
def about(request):
    return HttpResponse("this is about")
def contact(request):
    return HttpResponse("this is contact")