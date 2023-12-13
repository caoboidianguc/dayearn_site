from typing import Any
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from ledger.models import Khach, Service
from django.views.generic import ListView, View, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import DatHenFrom, ExistClientForm
from datetime import timedelta, datetime
from django.contrib import messages
from django.core.mail import EmailMessage


class DatHenView(ListView):
    template = 'datHen/list_dat_hen.html'
    def get(self, request):
        allHen = Khach.objects.filter(day_comes=datetime.today()).order_by("time_at")
        allKhachHen = {'khachHen': allHen}
        return render(request, self.template, allKhachHen)



    
    
class ExistClientHen(View):
    template = 'datHen/exist_client_hen.html'
    success_url = reverse_lazy('datHen:listHen')
    def get(self, request):
        khach = Khach.objects.filter(full_name=request.GET.get('full_name'), phone=request.GET.get('phone'))
        form = ExistClientForm()
        cont = {'formDatHen': form, 'khach': khach}
        return render(request, self.template, cont)
    
class ExistFound(View):
    template = 'datHen/exist_found.html'
    success_url = reverse_lazy('datHen:listHen')
    chuDe = "Dayearns Confirm schedule"
    def get(self, request, pk):
        khach = get_object_or_404(Khach, id=pk)
        form = DatHenFrom(instance=khach)
        cont = {'formDatHen': form}
        return render(request, self.template, cont)
    
    def post(self, request, pk):
        khach = get_object_or_404(Khach, id=pk)
        form = DatHenFrom(request.POST, instance=khach)
        if not form.is_valid():
            cont = {'formDatHen': form}
            return render(request, self.template, cont)
        khac = form.save(commit=False)
        khac.save()
        form.save_m2m()
        tinNhan = f"You scheduled with DayEarns \nOn: {form.instance.day_comes} \nAt: {form.instance.time_at} \nTechnician: {form.instance.technician}"
        messages.success(request, f"{form.instance.full_name} was scheduled successfully!")
        EmailMessage(self.chuDe, tinNhan, to=[form.instance.email]).send()
        return redirect(self.success_url)
    
    
class KhachLayHen(View):
    template = 'datHen/layhen.html'
    success_url = reverse_lazy('datHen:listHen')
    chuDe = "Dayearns Confirm schedule"
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
        tinNhan = f"You scheduled with DayEarns \nOn: {form.instance.day_comes} \nAt: {form.instance.time_at} \nTechnician: {form.instance.technician}"
        messages.success(request, f"{form.instance.full_name} was scheduled successfully!")
        EmailMessage(self.chuDe, tinNhan, to=[form.instance.email]).send()
        return redirect(self.success_url)
    
