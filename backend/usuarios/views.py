from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Usuario

def listar_usuarios(request):
    usuarios = list(Usuario.objects.values('id', 'nome', 'email', 'ativo'))
    return JsonResponse(usuarios, safe=False)

def buscar_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    data = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "ativo": usuario.ativo
    }
    return JsonResponse(data)