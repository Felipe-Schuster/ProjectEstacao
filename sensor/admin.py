from django.contrib import admin
from .models import SensorData, Configuracao


@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('id','token',)

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'temperatura_dht', 'umidade', 'temperatura_bmp', 'pressao_bmp', 'anemometro', 'biruta', 'pluviometro')
    list_per_page = 20
    