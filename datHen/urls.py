from django.urls import path
from .views import DatHenView, KhachLayHen, FindClient, ExistFound, FirstStep, Second


app_name = "datHen"
urlpatterns = [
    path('all/', DatHenView.as_view(), name='listHen' ),
    path('schedule/', KhachLayHen.as_view(), name='schedule' ),
    path('get_client/', FindClient.as_view(), name='find_client' ),
    path('existclient/<int:pk>/', ExistFound.as_view(), name='exist_found' ),
    path('first_step/', FirstStep.as_view(), name='first_step' ),
    path('tech/<int:pk>/', Second.as_view(), name='technician_detail' ),
]
