from django.db import models

# classe usuário que irá se transformar na tabela de banco de dados
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

