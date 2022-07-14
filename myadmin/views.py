from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from phongthuy_thanhnhan.funcs import *

def index(request):
    # check had logged
    if check_login(request):
        return render(request,"myadmin/index.html")
    else:
        return render(request,"myadmin/login.html")

def login(request):
    print('login')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:        
                obj_json = {
                    "success": True
                }
                request.session['admin'] = 'admin'
                return HttpResponseRedirect("/myadmin")
            else:
                return render(request,"myadmin/login.html", {"status":False})
        else:
            return render(request,"myadmin/login.html", {"status":False})

    return render(request,"myadmin/login.html")

def danhmuc(request):
    print('danhmuc')
    return render(request,"myadmin/danhmuc.html")