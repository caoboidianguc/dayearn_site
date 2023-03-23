from django.urls import path
from . import views


app_name = 'ledger'
urlpatterns = [
    path('', views.AllEmployee.as_view(), name="index"),
]
