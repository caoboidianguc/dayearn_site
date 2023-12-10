from django import forms
from datetime import timedelta, date
from ledger.models import Khach
from phonenumber_field.modelfields import PhoneNumberField


class ChonNgay(forms.widgets.DateInput):
    input_type = 'date'
    
    
class DatHenFrom(forms.ModelForm):

    day_comes = forms.DateField(widget=ChonNgay(attrs={'min': date.today()}))
    time_at = forms.TimeField(widget=ChonNgay(attrs={'type': 'time'}))
    email = forms.CharField(
        required=False,
        widget=forms.widgets.EmailInput(attrs={'placeholder':'Optional'}))
    phone = PhoneNumberField()
    class Meta:
        
        model = Khach
        fields = ['full_name', 'phone', 'email', 'day_comes', 'time_at', 'technician']
        
        
        
        
