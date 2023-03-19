from django.db import models
from django.conf import settings



# Create your models here.
    
class Technician(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    dskhach = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Khach', related_name='tech_client')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
class Khach(models.Model):
    full_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=35, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    