from django import forms
from .models import Technician, Khach, Service
from django.contrib.auth.forms import UserCreationForm



class TechForm(forms.ModelForm):
    
    class Meta:
        model = Technician
        fields = ["name","phone"]


class ClientForm(forms.ModelForm):
    """Form definition for Client."""

    class Meta:
        """Meta definition for Clientform."""
        model = Khach
        fields = ['full_name', 'phone','email', 'technician']

    
class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ['dichVu','gia','time_serv']


class TaiKhoanCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)