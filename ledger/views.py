from django.shortcuts import render
from .models import Technician, Khach, Service
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.

class AllEmployee(LoginRequiredMixin, View):
    template = 'ledger/index.html'
    def get(self,request):
        employee = Technician.objects.all()
        cont = {'employees': employee}
        return render(request, self.template, cont)
    
class AllServices(LoginRequiredMixin, View):
    template = ''
    def get(self, request):
        serv = Service.objects.all()
        cont = {'dvu': serv}
        return render(request,self.template,cont)