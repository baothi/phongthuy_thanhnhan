from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms import ModelForm
from myadmin.models import *
from django.forms import ModelChoiceField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class NameChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.ten}'

class danhsachtintuc_form(ModelForm):
    ten = forms.CharField(max_length=255, widget=forms.TextInput(), required=True)
    mieuta = forms.CharField(max_length=4096, widget=forms.Textarea({'rows':'3', 'style': 'width:100%;'}), required=True)
    class Meta:
        model = danhsachtintuc
        fields = '__all__'
        exclude = []
        widgets = {
            'ten': forms.TextInput(attrs={'style': 'width:100%;'}),
            'mieuta': forms.Textarea(attrs={'rows':'3', 'style': 'width:100%;'}),
        }

    def __init__(self, *args, **kwargs):
        super(danhsachtintuc_form, self).__init__(*args, **kwargs)
        CONTAINER_STATUS_CHOICES = (
            ("1", "Hoạt Động"),
            ("0", "Không Hoạt Động")
        )
        self.fields['trangthai'] = forms.ChoiceField(choices=CONTAINER_STATUS_CHOICES, widget=forms.Select(attrs={}))
        
class baiviet_form(ModelForm):
    danhsachtintuc = NameChoiceField(queryset=danhsachtintuc.objects.filter(trangthai=True), required=True)
    ten = forms.CharField(max_length=255, widget=forms.TextInput(), required=True)
    hinhanh = forms.FileField(required=False)
    mieuta = forms.CharField(max_length=4096, widget=forms.Textarea({'rows':'3', 'style': 'width:100%;'}), required=False)
    noidung = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = baiviet
        fields = '__all__'
        exclude = []
        widgets = {
            'ten': forms.TextInput(attrs={'style': 'width:100%;', 'required':'true'}),
            'mieuta': forms.Textarea(attrs={'rows':'3', 'style': 'width:100%;'}),
        }

    def __init__(self, *args, **kwargs):
        super(baiviet_form, self).__init__(*args, **kwargs)
        CONTAINER_STATUS_CHOICES = (
            ("1", "Hoạt Động"),
            ("0", "Không Hoạt Động")
        )
        self.fields['trangthai'] = forms.ChoiceField(choices=CONTAINER_STATUS_CHOICES, widget=forms.Select(attrs={}))