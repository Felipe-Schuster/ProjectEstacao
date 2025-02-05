from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer
from .decorators import token_required
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# View baseada em classe para listar os últimos 20 registros
class SensorDataAPIView(APIView):
    def get(self, request):
        try:
            # Obtém os últimos 20 registros ordenados por timestamp
            data = SensorData.objects.all().order_by('-timestamp')[:20]
            if not data:
                return Response(
                    {"status": "success", "message": "Nenhum dado encontrado."},
                    status=status.HTTP_200_OK,
                )
            # Serializa os dados
            serializer = SensorDataSerializer(data, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"status": "error", "message": "Erro ao buscar dados."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# View baseada em função para receber dados via POST
@api_view(["POST"])
@token_required
def sensor_api(request):
    try:
        # Passa os dados da requisição para o serializador
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            # Salva os dados no banco
            serializer.save()
            return Response(
                {"status": "success", "message": "Dados enviados com sucesso."},
                status=status.HTTP_201_CREATED,
            )
        # Retorna erros de validação
        return Response(
            {"status": "error", "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as e:
        print(e)
        return Response(
            {"status": "error", "message": "Erro interno no servidor."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# View para renderizar a página HTML
def index(request):
    try:
        # Obtém o último registro de SensorData
        ultimo_dado = SensorData.objects.latest('timestamp')
    except SensorData.DoesNotExist:
        ultimo_dado = None  # Retorna None se não houver registros
    return render(request, 'index.html', {'ultimo_dado': ultimo_dado})