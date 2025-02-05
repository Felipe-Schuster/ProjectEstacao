# Generated by Django 5.1.1 on 2025-02-05 21:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configuracao',
            options={'verbose_name': 'Configuração', 'verbose_name_plural': 'Configurações'},
        ),
        migrations.AlterModelOptions(
            name='sensordata',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Dado do Sensor', 'verbose_name_plural': 'Dados dos Sensores'},
        ),
        migrations.AddField(
            model_name='configuracao',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='configuracao',
            name='token',
            field=models.CharField(max_length=255, verbose_name='Token de Autenticação'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='anemometro',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Velocidade do Vento (m/s)'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='biruta',
            field=models.CharField(choices=[('N', 'Norte'), ('S', 'Sul'), ('L', 'Leste'), ('O', 'Oeste')], max_length=1, verbose_name='Direção do Vento'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='pluviometro',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Volume de Chuva (mm)'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='pressao_bmp',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(800), django.core.validators.MaxValueValidator(1200)], verbose_name='Pressão BMP (hPa)'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='temperatura_bmp',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-40), django.core.validators.MaxValueValidator(80)], verbose_name='Temperatura BMP (°C)'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='temperatura_dht',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-40), django.core.validators.MaxValueValidator(80)], verbose_name='Temperatura DHT (°C)'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='Data e Hora'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='umidade',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Umidade (%)'),
        ),
    ]
