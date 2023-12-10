from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField




    
class Technician(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clients = models.ForeignKey("Khach", on_delete=models.CASCADE, null=True, related_name='client')
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
class Khach(models.Model):
    class Status(models.TextChoices):
        online = "WebSite"
        call = "Phone Call"
        cancel = "Cancel"
        arrived = "Arrived"
        
    full_name = models.CharField(max_length=25)
    phone = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(max_length=35, null=True, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True, blank=True)
    diem = models.PositiveIntegerField(default=0)
    ngaydau = models.DateTimeField(editable=False,auto_now_add=True)
    day_comes = models.DateField()
    time_at = models.TimeField()
    desc = models.TextField(max_length=250,blank=True, null=True)
    services = models.ForeignKey("Service", on_delete=models.DO_NOTHING, null=True, blank=True)
    comeBy = models.CharField(choices=Status.choices, max_length=12, default=Status.online)

    def __str__(self) -> str:
        return self.full_name
    def save(self, *args, **kwargs):
        self.diem += 1
        super().save(*args,**kwargs)
    
    
class Service(models.Model):
    dichVu = models.CharField(max_length=30)
    gia = models.FloatField()
    thoiLuong = models.DurationField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.dichVu
    
    
    