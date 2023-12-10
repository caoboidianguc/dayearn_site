from django.urls import path
from .views import DatHenView, KhachLayHen


app_name = "datHen"
urlpatterns = [
    path('all/', DatHenView.as_view(), name='listHen' ),
    path('schedule/', KhachLayHen.as_view(), name='schedule' ),
]
