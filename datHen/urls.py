from django.urls import path
from .views import DatHenView, KhachLayHen, ExistClientHen, ExistFound


app_name = "datHen"
urlpatterns = [
    path('all/', DatHenView.as_view(), name='listHen' ),
    path('schedule/', KhachLayHen.as_view(), name='schedule' ),
    path('get_client/', ExistClientHen.as_view(), name='exist_client' ),
    path('existclient/<int:pk>/', ExistFound.as_view(), name='exist_found' ),
]
