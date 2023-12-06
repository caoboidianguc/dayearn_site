from django import forms
from .models import DatHen


class DatHenFrom(forms.ModelForm):
    class Meta:
        model = DatHen
        fields = ['ngayhen','vaoLuc', 'tech']
        
        
        

