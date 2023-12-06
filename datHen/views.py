from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import DatHen
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import DatHenFrom
from ledger.forms import ClientForm

class DatHenView(ListView):
    template = 'datHen/list_dat_hen.html'
    def get(self, request):
        allHen = DatHen.objects.all()
        allKhachHen = {'khachHen': allHen}
        return render(request, self.template, allKhachHen)
        

class KhachLayHen(View):
    template = 'datHen/layhen.html'
    success_url = reverse_lazy('ledger:index')
    def get(self, request):
        form = DatHenFrom()
        cont = {'formDatHen': form}
        return render(request, self.template, cont)
    

class Client(View):
    template = 'datHen/client_form.html'
    success_url = reverse_lazy('datHen:layhen')
    def get(self, request):
        form = ClientForm()
        cont = {'formClient': form}
        return render(request, self.template, cont)
    
    
    
    
    
