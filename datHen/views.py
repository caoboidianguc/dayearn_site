from django.shortcuts import render
from .models import DatHen
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



class DatHenView(ListView):
    template = 'datHen/list_dat_hen.html'
    def get(self, request):
        allHen = DatHen.objects.all()
        allKhachHen = {'khachHen': allHen}
        return render(request, self.template, allKhachHen)
        