from django.db import models
from django.contrib.auth.models import User

class danhsachtintuc(models.Model):
    ten = models.CharField(max_length=255, null=True, blank=True) 
    mieuta = models.CharField(max_length=4096, null=True, blank=True) 
    trangthai = models.BooleanField(default=True, blank=True)
    ngaytao = models.DateTimeField(null=True, blank=True)


class baiviet(models.Model):
    danhsachtintuc = models.ForeignKey(danhsachtintuc, related_name='dmtt', on_delete=models.SET_NULL, null=True, blank=True)
    ten = models.CharField(max_length=255, null=True, blank=True) 
    hinhanh = models.CharField(max_length=255, null=True, blank=True)
    mieuta = models.CharField(max_length=4096, null=True, blank=True) 
    noidung = models.CharField(max_length=20096, null=True, blank=True) 
    trangthai = models.BooleanField(default=True, blank=True)
    ngaytao = models.DateTimeField(null=True, blank=True)    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
