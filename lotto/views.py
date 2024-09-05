from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import GuessNumbers
from django.shortcuts import render, redirect

def index(request):
 return render(request, 'lotto/default.html', {})

def hello(request) :
        return HttpResponse('<h1 style = "color:red">Hello, world!</h1>')