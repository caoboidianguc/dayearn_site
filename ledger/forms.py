from django import forms
from .models import Technician, Khach, Service



class TechForm(forms.ModelForm):
    
    class Meta:
        model = Technician
        fields = ["name","phone"]


class ClientForm(forms.ModelForm):
    """Form definition for Client."""

    class Meta:
        """Meta definition for Clientform."""
        model = Khach
        fields = ['full_name', 'phone','email']

    
class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ['dichVu','gia']
