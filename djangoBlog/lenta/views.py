from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_method(text):
    if True:
        return HttpResponse(text + ' (GET)')
    else:
        return HttpResponse(text + ' (POST)')

def show_lenta(request):
    return show_method('Hello, World!')

def add_like(request):
    return show_method('Added like')

def add_comment(request):
    return show_method('Added comment')
