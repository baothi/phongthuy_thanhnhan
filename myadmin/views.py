import os
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from phongthuy_thanhnhan.funcs import *
from myadmin.forms import *
from django.conf import settings

def index(request):
    # check had logged
    print('danhmuc==========')
    if check_login(request):
        return render(request,"myadmin/index.html")
    else:
        return HttpResponseRedirect("/myadmin/login")

def login(request):
    print('login')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('user==========',user)
            if user.is_active:        
                obj_json = {
                    "success": True
                }
                print('user is_active==========',user.is_active)
                request.session['admin'] = 'admin'
                return HttpResponseRedirect("/myadmin")
            else:
                return render(request,"myadmin/login.html", {"status":False})
        else:
            return render(request,"myadmin/login.html", {"status":False})

    return render(request,"myadmin/login.html")

# ============================ Danh Muc ==============================
def danhmuc(request):
    print('danhmuc')
    # check had logged
    if check_login(request):
        danhmuc_list = danhsachtintuc.objects.all().order_by('-trangthai','ngaytao')
        return render(request,"myadmin/danhmuc.html",{"danhmuc_list":danhmuc_list})
    else:
        return HttpResponseRedirect("/myadmin/login")

def danhmuc_tao(request):
    print('danhmuc tao')
    # check had logged
    if check_login(request):
        if request.method == "POST":
            mform = danhsachtintuc_form(request.POST)
            if mform.is_valid():
                new_model = mform.save(commit=False)
                new_model.ngaytao = datetime.now()                
                status = True
                if str(request.POST['trangthai']) == '0':
                    status = False                 
                new_model.trangthai = status
                new_model.save()
                return HttpResponseRedirect("/myadmin/danhmuc")
            else:
                print(mform.errors)
        else:
            dm_form = danhsachtintuc_form(instance=danhsachtintuc())
            return render(request,"myadmin/danhmuc_tao.html", {"dm_form":dm_form})
    else:
        return HttpResponseRedirect("/myadmin/login")

def danhmuc_sua(request, danhmuc_id):
    print('danhmuc sua')
    # check had logged
    if check_login(request):
        obj_model = danhsachtintuc.objects.get(id=danhmuc_id)
        if request.method == "POST":
            mform = danhsachtintuc_form(request.POST or None, instance=obj_model)
            if mform.is_valid():
                obj_model.ten =  request.POST['ten']
                obj_model.mieuta =  request.POST['mieuta']               
                status = True
                if str(request.POST['trangthai']) == '0':
                    status = False                 
                obj_model.trangthai = status
                obj_model.save()
                return HttpResponseRedirect("/myadmin/danhmuc")
            else:
                print(mform.errors)
        else:
            dm_form = danhsachtintuc_form(instance=obj_model)
            return render(request,"myadmin/danhmuc_sua.html", {"dm_form":dm_form,"danhmuc_id":danhmuc_id,"obj_model":obj_model})
    else:
        return HttpResponseRedirect("/myadmin/login")

def danhmuc_xoa(request, danhmuc_id):
    print('danhmuc xoa')
    # check had logged
    if check_login(request):
        try:
            obj_model = danhsachtintuc.objects.get(id=danhmuc_id)
            obj_model.trangthai = False
            obj_model.save()
        except:
            pass
        return HttpResponseRedirect("/myadmin/danhmuc")
    else:
        return HttpResponseRedirect("/myadmin/login")
    
# ============================ Bai Viet ==============================
def baiviet_index(request):
    print('baiviet')
    # check had logged
    if check_login(request):
        baiviet_list = baiviet.objects.all().order_by('-trangthai','ngaytao')
        return render(request,"myadmin/baiviet.html",{"baiviet_list":baiviet_list})
    else:
        return HttpResponseRedirect("/myadmin/login")

def baiviet_tao(request):
    print('baiviet tao')
    # check had logged
    if check_login(request):
        if request.method == "POST":
            mform = baiviet_form(request.POST)
            if mform.is_valid():
                fpath = ''
                if request.FILES:                  
                    filesize=0
                    for f in request.FILES.getlist('hinhanh'):
                        filesize=filesize+ f.size
                    if filesize <  10000000:
                        for f in request.FILES.getlist('hinhanh'):
                            curr_dt = datetime.now()
                            timestamp = str(round(curr_dt.timestamp()))
                            filename = timestamp+'_'+f.name
                            mediaPtah = os.path.join(settings.MEDIA_ROOT,'news')
                            fpath = os.path.join(mediaPtah, filename)
                            open(fpath, 'wb').write(f.file.read())
                new_model = mform.save(commit=False)
                new_model.ngaytao = datetime.now()                
                status = True
                if str(request.POST['trangthai']) == '0':
                    status = False    
                new_model.hinhanh = fpath             
                new_model.trangthai = status
                new_model.save()
                return HttpResponseRedirect("/myadmin/baiviet")
            else:
                print(mform.errors)
        else:
            dm_form = baiviet_form(instance=baiviet())
            return render(request,"myadmin/baiviet_tao.html", {"dm_form":dm_form})
    else:
        return HttpResponseRedirect("/myadmin/login")

def baiviet_sua(request, baiviet_id):
    print('baiviet sua')
    # check had logged
    if check_login(request):
        obj_model = baiviet.objects.get(id=baiviet_id)
        if request.method == "POST":
            mform = baiviet_form(request.POST or None, instance=obj_model)
            if mform.is_valid():
                fpath = ''
                if request.FILES:                  
                    filesize=0
                    for f in request.FILES.getlist('hinhanh'):
                        filesize=filesize+ f.size
                    if filesize <  10000000:
                        for f in request.FILES.getlist('hinhanh'):
                            curr_dt = datetime.now()
                            timestamp = str(round(curr_dt.timestamp()))
                            filename = timestamp+'_'+f.name
                            fpath = os.path.join(settings.MEDIA_ROOT + '/news/', filename)
                            open(fpath, 'wb').write(f.file.read())
                obj_model.ten =  request.POST['ten']                
                obj_model.hinhanh = fpath
                obj_model.mieuta =  request.POST['mieuta']   
                obj_model.noidung =  request.POST['noidung']             
                status = True
                if str(request.POST['trangthai']) == '0':
                    status = False                 
                obj_model.trangthai = status
                obj_model.save()
                return HttpResponseRedirect("/myadmin/baiviet")
            else:
                print(mform.errors)
        else:
            dm_form = baiviet_form(instance=obj_model)
            return render(request,"myadmin/baiviet_sua.html", {"dm_form":dm_form,"baiviet_id":baiviet_id,"obj_model":obj_model})
    else:
        return HttpResponseRedirect("/myadmin/login")

def baiviet_xoa(request, baiviet_id):
    print('baiviet xoa')
    # check had logged
    if check_login(request):
        try:
            obj_model = baiviet.objects.get(id=baiviet_id)
            obj_model.trangthai = False
            obj_model.save()
        except:
            pass
        return HttpResponseRedirect("/myadmin/baiviet")
    else:
        return HttpResponseRedirect("/myadmin/login")
