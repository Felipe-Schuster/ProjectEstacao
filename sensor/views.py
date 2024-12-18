from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer
from .decorators import token_required
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class SensorDataAPIView(APIView):
    def get(self, request):
        data = SensorData.objects.all().order_by('-timestamp')[:10]  # Últimos 10 registros
        serializer = SensorDataSerializer(data, many=True)
        return Response(serializer.data)


    @api_view(["POST"])
    @token_required
    def sensor_api(request):
        """
        Endpoint para receber dados de sensores via POST.
        """
        try:
            serializer = SensorDataSerializer(data=request.data)  # Passa os dados da requisição ao serializer
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "success", "message": "Dados enviados com sucesso."},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {"status": "error", "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            print(e)


def index(request):
    """
    View para renderizar o template principal com o último dado registrado.
    """
    try:
        ultimo_dado = SensorData.objects.latest('timestamp')  # Ordena pelo timestamp e pega o mais recente
    except SensorData.DoesNotExist:
        ultimo_dado = None  # Retorna None se não houver registros
    return render(request, 'index.html', {'ultimo_dado': ultimo_dado})
