from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as xem


app_name = 'ledger'
urlpatterns = [
    path('', views.AllEmployee.as_view(), name="index"),
    path('add_employee/', views.EmpCreate.as_view(), name="add_employee"),
    path('register/', views.TaoTaiKhoan.as_view(), name="register"),
    path('services/', views.AllServices.as_view(), name="services"),
    path('add_services/', views.AddService.as_view(), name="add_service"),
]
