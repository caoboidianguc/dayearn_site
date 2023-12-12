from django import forms
from .models import Technician, Khach, Service
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField


class TechForm(forms.ModelForm):
    phone = PhoneNumberField()
    class Meta:
        model = Technician
        fields = ["name","phone"]


class ClientForm(forms.ModelForm):
    email = forms.CharField(required=False)
    class Meta:
        """Meta definition for Clientform."""
        model = Khach
        fields = ['full_name', 'phone', 'email', 'services']
        

    
class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ['dichVu','gia']


class TaiKhoanCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
        

