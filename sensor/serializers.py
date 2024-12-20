from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = [  'id', 'temperatura_dht', 'umidade', 'pressao_bmp', 'temperatura_bmp', 'pluviometro','anemometro','biruta']
        

    def validate_temperatura_dht(self, value):
        if value < -40 or value > 80:
            raise serializers.ValidationError("Temperatura DHT fora do intervalo esperado.")
        return value

    def validate_umidade(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Umidade deve estar entre 0 e 100%.")
        return value

    def validade_pressao_bmp(self, value):
        if value < 800 or value > 1200:
            raise serializers.ValidationError("Pressão BMP fora do intervalo esperado.")
        return value
