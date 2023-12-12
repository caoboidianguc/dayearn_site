from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from ledger.models import Khach, Service
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from .forms import DatHenFrom
from ledger.forms import ClientForm
from datetime import timedelta, datetime


class DatHenView(ListView):
    template = 'datHen/list_dat_hen.html'
    def get(self, request):
        allHen = Khach.objects.filter(day_comes=datetime.today())
        ser = list()
        for khach in allHen:
            ser = [dv for dv in khach.services.all()]
        allKhachHen = {'khachHen': allHen, 'dichvu': ser}
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
        khac = form.save(commit=False)
        khac.save()
        form.save_m2m()
        return redirect(self.success_url)
    


