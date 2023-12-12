from django.urls import path, re_path, include
from ledger.views import AllEmployee, EmpCreate, TaoTaiKhoan, AllServices, AddService
from django.contrib.auth import views as xem


app_name = 'ledger'
urlpatterns = [
    path('', AllEmployee.as_view(), name="index"),
    path('ledger/add_employee/', EmpCreate.as_view(), name="add_employee"),
    path('ledger/register/', TaoTaiKhoan.as_view(), name="register"),
    path('ledger/services/', AllServices.as_view(), name="services"),
    path('ledger/services/add_services/', AddService.as_view(), name="add_service"),
    # path('dathen/<int:pk>/detail/', views.DatHenChiTiet.as_view(), name="dathen_detail"),
    
]
