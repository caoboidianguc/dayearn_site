from django import forms
from .models import DatHen
from datetime import timedelta, date
from ledger.models import Khach


class ChonNgay(forms.widgets.DateInput):
    input_type = 'date'
    
    
class DatHenFrom(forms.ModelForm):

    ngayhen = forms.DateField(widget=ChonNgay(attrs={'min': date.today()}))
    vaoluc = forms.TimeField(widget=ChonNgay(attrs={'type': 'time'}))
    
    class Meta:
        # model = DatHen
        model = Khach
        fields = ['full_name', 'phone', 'email', 'ngayhen', 'vaoluc']
        
        
        
        
