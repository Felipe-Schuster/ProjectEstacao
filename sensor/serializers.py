from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = [
            'id', 'temperatura_dht', 'umidade', 'pressao_bmp',
            'temperatura_bmp', 'pluviometro', 'anemometro', 'biruta'
        ]

    def validate_temperatura_dht(self, value):
        """
        Valida se a temperatura do DHT está dentro do intervalo esperado (-40°C a 80°C).
        """
        if value < -10 or value > 80:
            raise serializers.ValidationError("Temperatura DHT fora do intervalo esperado.")
        return value

    def validate_umidade(self, value):
        """
        Valida se a umidade está dentro do intervalo esperado (0% a 100%).
        """
        if value < 0 or value > 100:
            raise serializers.ValidationError("Umidade deve estar entre 0 e 100%.")
        return value

    def validate_pressao_bmp(self, value):
        """
        Valida se a pressão do BMP está dentro do intervalo esperado (800 hPa a 1200 hPa).
        """
        if value < 800 or value > 1200:
            raise serializers.ValidationError("Pressão BMP fora do intervalo esperado.")
        return value

    def validate_anemometro(self, value):
        """
        Valida se a velocidade do vento (anemômetro) é um valor positivo.
        """
        if value < 0:
            raise serializers.ValidationError("Velocidade do vento não pode ser negativa.")
        return value

    def validate_pluviometro(self, value):
        """
        Valida se o volume de chuva (pluviômetro) é um valor positivo.
        """
        if value < 0:
            raise serializers.ValidationError("Volume de chuva não pode ser negativo.")
        return value

    def validate_biruta(self, value):
        """
        Valida se a direção do vento (biruta) é uma das opções esperadas.
        """
        direcoes_validas = ["N", "S", "L", "O"]
        if value not in direcoes_validas:
            raise serializers.ValidationError(f"Direção do vento inválida. Use uma das opções: {direcoes_validas}.")
        return value