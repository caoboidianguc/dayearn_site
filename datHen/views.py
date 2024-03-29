from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from ledger.models import Khach, Technician
from django.views.generic import View, ListView
from django.urls import reverse_lazy
from .forms import DatHenFrom, ExistClientForm, FirstStepForm, SecondStepForm
from datetime import datetime, timedelta
from django.contrib import messages
from django.core.mail import EmailMessage
# from django.views.generic.dates import DayArchiveView


class DatHenView(View):
    template_name = 'datHen/dathenview.html'
    def get(self, request):
        hnay = Khach.objects.filter(day_comes=datetime.today()).order_by("time_at")
        allKhachHen = {'khachHen': hnay }
        return render(request, self.template_name, allKhachHen)

# https://docs.djangoproject.com/en/5.0/ref/models/querysets/#field-lookups

    
class FindClient(View):
    template = 'datHen/exist_client_hen.html'
    success_url = reverse_lazy('datHen:listHen')
    def get(self, request):
        name = str(request.GET.get('full_name')).upper()
        khach = Khach.objects.filter(full_name=name,phone=request.GET.get('phone'))
        form = ExistClientForm()
        cont = {'formDatHen': form, 'khach': khach}
        return render(request, self.template, cont)
    
class ExistFound(View):
    template = 'datHen/layhen.html'
    success_url = reverse_lazy('datHen:listHen')
    chuDe = "Dayearns Confirm schedule"
    def get(self, request, pk):
        khach = get_object_or_404(Khach, id=pk)
        form = DatHenFrom(instance=khach)
        cont = {'formDatHen': form}
        return render(request, self.template, cont)
    
    def post(self, request, pk):
        tech = Technician.objects.all()
        khach = get_object_or_404(Khach, id=pk)
        form = DatHenFrom(request.POST, instance=khach)
        if not form.is_valid():
            cont = {'formDatHen': form}
            return render(request, self.template, cont)
        khac = form.save(commit=False)
        khac.save()
        form.save_m2m()
        if form.instance.status == "Cancel":
            tinNhan = "You had canceled. Thanks!"
        else:
            tinNhan = f"You scheduled with DayEarns \nOn: {form.instance.day_comes} \nAt: {form.instance.time_at} \nTechnician: {form.instance.technician}"
        messages.success(request, f"{form.instance.full_name} was scheduled successfully!")
        EmailMessage(self.chuDe, tinNhan, to=[form.instance.email]).send()
        thongbao = f"{form.instance.full_name} book appointment with you on {form.instance.day_comes} at {form.instance.time_at}"
        if form.instance.technician != None:
            for empl in tech:
                if form.instance.technician == empl:
                    EmailMessage(self.chuDe, thongbao, to=[empl.email]).send()
        return redirect(self.success_url)
    
    
class KhachLayHen(View):
    template = 'datHen/layhen.html'
    success_url = reverse_lazy('datHen:listHen')
    chuDe = "Dayearns Confirm schedule"
    
    def get(self, request):
        form = DatHenFrom()
        #needs more work for each Tech with time available
        cont = {'formDatHen': form}
        return render(request, self.template, cont)
    
    def post(self, request):
        tech = Technician.objects.all()
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
        thongbao = f"{form.instance.full_name} book appointment with you on {form.instance.day_comes} at {form.instance.time_at}"
        if form.instance.technician != None:
            for empl in tech:
                if form.instance.technician == empl:
                    EmailMessage(self.chuDe, thongbao, to=[empl.email]).send()
        return redirect(self.success_url)



class Second(View):
    template = 'datHen/second.html'
    success_url = reverse_lazy('datHen:listHen')
    
    def get(self, request, pk):
        techDetail = get_object_or_404(Technician, id=pk)        
        secondForm = SecondStepForm()
        allKhach = techDetail.get_clients()
        ngay = request.GET.get('day_comes')
        hnay = allKhach.filter(day_comes=datetime.today())
        khach_chon = allKhach.filter(day_comes=ngay).order_by('time_at')
        cont = {'techDetail': techDetail,
                'allKhach': allKhach,
                'secondForm': secondForm,
                'hnay': hnay,
                'hen': khach_chon,
            }
        
        return render(request, self.template, cont)
    
    
class FirstStep(View):
    template = 'datHen/first_step.html'
    success_url = reverse_lazy('datHen:listHen')
    chuDe = "Dayearns Confirm schedule"
    tech = Technician.objects.all()
    def get(self,request):
        cont = {'tech': self.tech}
        return render(request, self.template, cont)
    
    
    # def post(self, request):
    #     tech = Technician.objects.all()
    #     form = DatHenFrom(request.POST)
    #     form.instance.technician = self.first.instance.technician
    #     form.instance.services = self.first.instance.services
    #     form.instance.full_name = self.second.instance.full_name
    #     form.instance.phone = self.second.instance.phone
    #     form.instance.email = self.second.instance.email
    #     form.instance.day_comes = self.second.instance.day_comes
    #     form.instance.time_at = self.second.instance.time_at
    #     form.instance.sattus = self.second.instance.sattus
    #     if not form.is_valid():
    #         cont = {'first_step': self.first,
    #             'second_step': self.second}
    #         return render(request, self.template, cont)
    #     khac = form.save(commit=False)
    #     khac.save()
    #     form.save_m2m()
    #     tinNhan = f"You scheduled with DayEarns \nOn: {form.instance.day_comes} \nAt: {form.instance.time_at} \nTechnician: {form.instance.technician}"
    #     messages.success(request, f"{form.instance.full_name} was scheduled successfully!")
    #     EmailMessage(self.chuDe, tinNhan, to=[form.instance.email]).send()
    #     thongbao = f"{form.instance.full_name} book appointment with you on {form.instance.day_comes} at {form.instance.time_at}"
    #     if form.instance.technician != None:
    #         for empl in tech:
    #             if form.instance.technician == empl:
    #                 EmailMessage(self.chuDe, thongbao, to=[empl.email]).send()
    #     return redirect(self.success_url)
    
