from typing import Any
from django import forms
from datetime import timedelta, date, datetime
from ledger.models import Khach, Service
from phonenumber_field.modelfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


# class ChonTime(forms.widgets.TimeInput):
#     input_type = 'time'
    
class ChonNgay(forms.widgets.DateInput):
    input_type = 'date'
    
# class Lich(forms.ModelForm):
#     chonNgay = forms.DateField(widget=ChonNgay())
    
    
class DatHenFrom(forms.ModelForm):
    
    day_comes = forms.DateField(widget=ChonNgay(attrs={'min': date.today()}))
    
    time_at = forms.TimeField(widget=ChonNgay(attrs={'type': 'time'}))
    
    email = forms.CharField(
        required=False,
        widget=forms.widgets.EmailInput(attrs={'placeholder':'Optional'}))
    
    phone = PhoneNumberField()
    
    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all() ,widget=forms.CheckboxSelectMultiple())
    
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Full Name'
        }
    ))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    def clean_full_name(self):
        data = super().clean()
        data = self.cleaned_data['full_name']
        return str(data).upper()
        
    class Meta:
        
        model = Khach
        fields = ['technician', 'services', 'full_name', 'phone', 'email', 'day_comes', 'time_at', 'status']
        
        
        

class ExistClientForm(forms.ModelForm):
    
    class Meta:
        model = Khach
        fields = ['full_name','phone']
        
class FirstStepForm(forms.ModelForm):
    class Meta:
        model=Khach
        fields = ['technician']

class SecondStepForm(forms.ModelForm):
    day_comes = forms.DateField(widget=ChonNgay(attrs={'min': date.today()}))
    class Meta:
        model=Khach
        fields = [ 'day_comes', 'time_at','full_name', 'phone', 'email', 'status']
        
    def clean_full_name(self):
        data = super().clean()
        data = self.cleaned_data['full_name']
        return str(data).upper()