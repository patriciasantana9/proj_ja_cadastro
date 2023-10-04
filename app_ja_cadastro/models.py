from django.db import models

class Cadastrado(models.Model):
   id_cadastrado = models.AutoField(primary_key=True)
   gas = models.TextField(max_length=255)
   energia = models.TextField(max_length=255)
   agua = models.TextField(max_length=255)
   comida = models.TextField(max_length=255)
   aluguel = models.TextField(max_length=255)
   outros = models.TextField(max_length=255)
   