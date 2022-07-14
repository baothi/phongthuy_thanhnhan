import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
# from tutru.forms import *
# from tutru.models import *
# # Create your views here.
# from phongthuy.AmLich import *
from django.core import *
# import imgkit

def index(request):


    return render(request, "tutru/index.html")
