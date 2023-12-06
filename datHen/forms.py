from django import forms
from .models import DatHen
from datetime import timedelta

class DatHenFrom(forms.ModelForm):
    thoiLuong = forms.DurationField()
    class Meta:
        model = DatHen
        fields = ['ngayhen','vaoLuc', 'tech', 'khach']
        
        
        

