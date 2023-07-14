from django.db import models





# class DatHen(models.Model):
#     template = "ledger:dathen_detail"
    
#     khach = models.ForeignKey(Khach, on_delete=models.CASCADE, null=True)
#     ngayhen = models.DateField()
#     vaoLuc = models.TimeField()
#     services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    
#     def __str__(self) -> str:
#         return self.ngayhen.day
    
#     def get_absolute_url(self):
#         return reverse(self.template, args={"pk": self.pk})