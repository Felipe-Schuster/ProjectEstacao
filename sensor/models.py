from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class SensorData(models.Model):
    
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Data e Hora")
    temperatura_dht = models.FloatField(
        verbose_name="Temperatura DHT (°C)",
        validators=[MinValueValidator(-40), MaxValueValidator(80)]  # Intervalo válido para temperatura
    )
    umidade = models.FloatField(
        verbose_name="Umidade (%)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]  # Intervalo válido para umidade
    )
    temperatura_bmp = models.FloatField(
        verbose_name="Temperatura BMP (°C)",
        validators=[MinValueValidator(-40), MaxValueValidator(80)]  # Intervalo válido para temperatura
    )
    pressao_bmp = models.FloatField(
        verbose_name="Pressão BMP (hPa)",
        validators=[MinValueValidator(800), MaxValueValidator(1200)]  # Intervalo válido para pressão
    )
    anemometro = models.FloatField(
        verbose_name="Velocidade do Vento (m/s)",
        validators=[MinValueValidator(0)]  # Velocidade não pode ser negativa
    )
    biruta = models.CharField(
        max_length=1,
        verbose_name="Direção do Vento",
        choices=[('N', 'Norte'), ('S', 'Sul'), ('L', 'Leste'), ('O', 'Oeste')]  # Opções válidas
    )
    pluviometro = models.FloatField(
        verbose_name="Volume de Chuva (mm)",
        validators=[MinValueValidator(0)]  # Volume não pode ser negativo
    )

    def __str__(self):
      
        return f"Leitura em {self.timestamp}: {self.temperatura_dht}°C, {self.umidade}%, {self.pressao_bmp}hPa"

    class Meta:
        verbose_name = "Dado do Sensor"
        verbose_name_plural = "Dados dos Sensores"
        ordering = ['-timestamp']  # Ordena os registros por timestamp decrescente

# ClimaTempo API
class Configuracao(models.Model):
    
    token = models.CharField(max_length=255, verbose_name="Token de Autenticação")
    descricao = models.CharField(max_length=255, verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        
        return f"Configuração: {self.descricao or 'Sem descrição'}"

    class Meta:
        verbose_name = "Configuração"
        verbose_name_plural = "Configurações"