from django.db import models  # Importa o módulo models do Django
from django.utils import timezone  # Importa o módulo timezone do Django


class SensorData(models.Model):

    timestamp = models.DateTimeField(auto_now=True)  # Armazena a data e hora da leitura
    temperatura_dht = models.FloatField() # Armazena a temperatura do sensor DHT
    umidade = models.FloatField() # Armazena a umidade do sensor DHT
    temperatura_bmp = models.FloatField() # Armazena a temperatura do sensor BMP
    pressao_bmp = models.FloatField() # Armazena a pressão do sensor BMP
    anemometro = models.FloatField() # Armazena a velocidade do vento em m/s
    biruta = models.TextField() # Armazena a direção do vento
    pluviometro = models.FloatField() # Armazena a quantidade de  chuva em mm
   
    def __str__(self):
        return f"Leitura: {self.timestamp, self.temperatura_dht, self.umidade, self.temperatura_bmp, self.pressao_bmp, self.anemometro, self.biruta, self.pluviometro}"

class Configuracao(models.Model):
    token = models.CharField(max_length=255)

    def __str__(self):
        return f"Configuração: {self.token}"