from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string1(request):
    return HttpResponse('<h1>This is the string1 of app1</h1>')

def string2(request):
    return HttpResponse('<h1>This is the string2 of app1</h1>')
