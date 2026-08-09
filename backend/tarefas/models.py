from django.db import models
from usuarios.models import Usuario

class Tarefa(models.Model):
    usuario_responsavel = models.ForeignKey(
        Usuario, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )