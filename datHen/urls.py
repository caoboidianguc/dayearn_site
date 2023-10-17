from django.urls import path
from .views import DatHenView


app_name = "datHen"
urlpatterns = [
    path('all/', DatHenView.as_view(), name='listHen' ),
]
