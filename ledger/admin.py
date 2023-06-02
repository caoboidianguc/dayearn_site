from django.contrib import admin
from .models import Technician, Khach, Service, DatHen

# Register your models here.
admin.site.register(Technician)
admin.site.register(Khach)
admin.site.register(Service)
admin.site.register(DatHen)