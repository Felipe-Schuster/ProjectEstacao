from .models import Configuracao
from django.http import JsonResponse

def token_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Verifica se o token está presente no cabeçalho da requisição
        token = request.headers.get('Authorization')
        if token is None:
            return JsonResponse({'status': 'error', 'message': 'Token ausente.'}, status=403)
        
        # Verifica se o token corresponde ao token armazenado no banco de dados
        try:
            configuracao = Configuracao.objects.get(pk=1)  # Altere para a lógica adequada se necessário
            if token != configuracao.token:
                return JsonResponse({'status': 'error', 'message': 'Token inválido.'}, status=403)
        except Configuracao.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Configuração não encontrada.'}, status=404)

        return view_func(request, *args, **kwargs)

    return _wrapped_view
