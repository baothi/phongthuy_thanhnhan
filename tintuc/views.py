from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    print('tin tuc home')
    return render(request,"tintuc/index.html")