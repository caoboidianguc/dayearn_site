from django.shortcuts import render, redirect, get_object_or_404
from .models import Technician, Khach, Service
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views import View
from .forms import ClientForm, TechForm, ServiceForm
from django.urls import reverse_lazy



# Create your views here.

class AllEmployee(LoginRequiredMixin, ListView):
    template = 'ledger/index.html'
    def get(self,request):
        employee = Technician.objects.all()
        cont = {'employees': employee}
        return render(request, self.template, cont)
    
class AllServices(LoginRequiredMixin, ListView):
    # need a template for a list of all services
    template = ''
    def get(self, request):
        serv = Service.objects.all()
        cont = {'dvu': serv}
        return render(request,self.template,cont)
    
class EmpCreate(LoginRequiredMixin, View):
    template = 'ledger/add_employee.html'
    success_url = reverse_lazy('ledger:index')
    def get(self,request):
        form = TechForm()
        contx = {'form': form}
        return render(request, self.template, contx)
    def post(self, request):
        form = TechForm(request.POST)
        if not form.is_valid():
            cont = {'form': form}
            return render(request, self.template, cont)
        emp = form.save(commit=False)
        emp.owner = self.request.user
        emp.save()
        form.save_m2m
        return redirect(self.success_url)