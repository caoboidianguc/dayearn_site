from django.db import models
from django.conf import settings
from django.urls import reverse




# Create your models here.
    
class Technician(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clients = models.ForeignKey("Khach", on_delete=models.CASCADE, null=True, related_name='client')
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
class Khach(models.Model):
    full_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=35, null=True, blank=True)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True, blank=True)
    diem = models.PositiveIntegerField(default=0)
    ngay = models.DateTimeField(editable=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.TextField(max_length=250,blank=True, null=True)
    services = models.ForeignKey("Service", on_delete=models.DO_NOTHING, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.full_name
    def save(self, *args, **kwargs):
        self.diem += 1
        super().save(*args,**kwargs)
    
class Service(models.Model):
    dichVu = models.CharField(max_length=30)
    gia = models.FloatField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.dichVu
    
    
    