from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    telefone = models.IntegerField()
