from typing import Any
from django.shortcuts import render, redirect
from ledger.models import Khach
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from .forms import DatHenFrom
from ledger.forms import ClientForm
from datetime import timedelta, datetime


class DatHenView(ListView):
    template = 'datHen/list_dat_hen.html'
    def get(self, request):
        allHen = Khach.objects.filter(day_comes=datetime.today())
        allKhachHen = {'khachHen': allHen}
        return render(request, self.template, allKhachHen)
        

class KhachLayHen(View):
    template = 'datHen/layhen.html'
    success_url = reverse_lazy('datHen:listHen')
    
    def get(self, request):
        form = DatHenFrom()
        cont = {'formDatHen': form}
        return render(request, self.template, cont)
    
    def post(self, request):
        form = DatHenFrom(request.POST)
        if not form.is_valid():
            cont = {'formDatHen': form}
            return render(request, self.template, cont)
        
        form.save()
        return redirect(self.success_url)
    


