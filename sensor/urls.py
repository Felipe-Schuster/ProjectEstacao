from django.urls import path
from . import views

urlpatterns = [
    # URL para a função sensor_api (POST)
    path('api/sensor/', views.sensor_api, name='sensor_api'),

    # URL para a classe SensorDataAPIView (GET)
    path('api/sensors/', views.SensorDataAPIView.as_view(), name='sensor-data'),

    # URL para a página inicial (index)
    path('', views.index, name='index'),
]