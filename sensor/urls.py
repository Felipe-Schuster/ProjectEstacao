
from django.urls import path
from . import views

urlpatterns = [
    path('sensors/', views.SensorDataAPIView.sensor_api, name='sensor_api'),
    path('api/sensors', views.SensorDataAPIView.as_view(), name='sensor-data'),
    path('', views.index, name='index'),
]
