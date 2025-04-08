from django.db import models
from usuarios.models import Usuario

class Servico(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_final = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.servico} em {self.data_final.strftime('%d/%m/%Y')}"
