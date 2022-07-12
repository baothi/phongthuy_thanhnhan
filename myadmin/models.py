from django.db import models

class danhsachtintuc(models.Model):
    ten = models.CharField(max_length=255, null=True, blank=True) 
    mieuta = models.CharField(max_length=255, null=True, blank=True) 
    ngaytao = models.DateTimeField(null=True, blank=True)
