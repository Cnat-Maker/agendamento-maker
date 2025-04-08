from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ("V", "Visitante"),
        ("B", "Bolsista"),
    )
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default="V")

    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    matricula = models.CharField(max_length=14, null=True)

    def __str__(self):
        return self.username