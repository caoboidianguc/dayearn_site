from django.db import models
from ledger.models import Khach, Service, Technician
from datetime import timedelta



class DatHen(models.Model):
    class Status(models.TextChoices):
        online = "WebSite"
        call = "Phone Call"
        cancel = "Cancel"
        arrived = "Arrived"
    khach = models.ForeignKey(Khach, on_delete=models.DO_NOTHING)
    ngayhen = models.DateField()
    vaoLuc = models.TimeField()
    thoiLuong = models.DurationField()
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    comeBy = models.CharField(choices=Status.choices, max_length=12, default=Status.online)
    tech = models.OneToOneField(Technician, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.khach
    
   