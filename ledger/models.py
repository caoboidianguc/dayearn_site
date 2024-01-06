from typing import Any
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
import datetime
from datetime import timedelta




class Technician(models.Model):
    
    name = models.CharField(max_length=25)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=40, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    isWork = models.BooleanField(default=False)
    start_work_at = models.TimeField(null=True)
    end_work = models.TimeField(null=True)
    
    class Meta:
        unique_together = ('name','phone',)
        ordering = ['name']
    def clean(self):
        if self.start_work_at > self.end_work:
            raise ValidationError("Start time must be before end time")
    # technician_detail is the name will be create in url to retreat detail of Technician
    def get_absolute_url(self):
        return reverse("datHen:technician_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.name
    
    def get_clients(self):
        allClients = self.khachs.all()
        return allClients
        
    def get_day_off(self):
        return DayOff.objects.filter(tech=self)

        
    
    
class Khach(models.Model):
    class Status(models.TextChoices):
        online = "WebSite"
        cancel = "Cancel"
        
    full_name = models.CharField(max_length=25)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=40, null=True, blank=True)
    technician = models.ForeignKey(Technician, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='khachs')
    diem = models.PositiveIntegerField(default=0)
    ngaydau = models.DateTimeField(editable=False,auto_now_add=True)
    desc = models.TextField(max_length=250,blank=True, null=True)
    services = models.ManyToManyField("Service", blank=True, related_name="khachs")
    status = models.CharField(choices=Status.choices, max_length=12, default=Status.online)
    day_comes = models.DateField()
    time_at = models.TimeField()
    class Meta:
        unique_together = ('full_name','phone',)
        ordering = ['full_name','-day_comes']

    def __str__(self) -> str:
        return self.full_name
    
    def clean(self):
        if self.day_comes < datetime.date.today():
            raise ValidationError("Appointments should be in the future")
        if self.day_comes == datetime.date.today() and self.time_at < datetime.datetime.now().time():
            raise ValidationError("Your time for appointment was pass!")
     
    def get_services(self):
        ten = []
        for dv in self.services.all():
            ten.append(dv)
        return ten
    
    def get_time_done(sefl):
        tong = 0
        for service in sefl.services.all():
            tong += service.thoiGian.total_seconds()
        if tong > 0:
            tong = tong/60
            return tong
        return tong
    
    def get_done_at(self):
        gio = datetime.datetime(1970,1,1,hour=self.time_at.hour, minute=self.time_at.minute) + timedelta(minutes=self.get_time_done())
        return datetime.time(hour=gio.hour, minute=gio.minute)
    
    # def save(self, *args, **kwargs):
    #     self.full_name = self.full_name.upper()
    #     self.diem += 1
    #     return super(Khach, self).save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("datHen:exist_found", kwargs={"pk": self.pk})
    
    
    
    
class Service(models.Model):
    dichVu = models.CharField(max_length=30)
    gia = models.FloatField()
    thoiGian = models.DurationField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.dichVu
    def save(self, *kwag, **kwargs):
        if self.thoiGian <= timedelta(0):
            raise ValidationError("Time must be greater than  0 !")
        return super().save(*kwag, **kwargs)
    
# Service.khachs.all() <- ffrom Khach.services.models.manytomany
# class Appointment(models.Model):
    
#     tech = models.ManyToManyField(Technician, on_delete=models.DO_NOTHING, related_name='appointments')
#     service = models.ManyToManyField(Service, on_delete=models.DO_NOTHING)
#     khach = models.ForeignKey(Khach, on_delete=models.DO_NOTHING)
#     day_comes = models.DateField()
#     time_at = models.TimeField()
    
    # def clean(self):
    #     if self.start >= self.end:
    #         raise ValidationError("Start time must be before end time")
      



class DayOff(models.Model):
    tech = models.ForeignKey(Technician, on_delete=models.CASCADE, related_name="dayoff")
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.start_date} to {self.end_date} - {self.note if self.note else 'Day off'}"

    def clean(self):
        if self.start_date is not None and self.end_date is not None:
            if self.start_date > self.end_date:
                raise ValidationError("Start date must be before end date")
