from django.db import models
from usuarios.models import Usuario

class Servico(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    motivo = models.TextField(null=True)

    # Usando caracteres como código para o status
    STATUS_CHOICES = (
        ('S', 'Solicitado'),
        ('A', 'Andamento'),
        ('F', 'Finalizado')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='S')

    cliente = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='agendamentos_cliente'  # Nome exclusivo para a relação reversa de 'cliente'
    )
    bolsista = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        null=True,
        related_name='agendamentos_bolsista'  # Nome exclusivo para a relação reversa de 'bolsista'
    )

    data_prevista = models.DateField()
    data_final = models.DateField(null=True)
    data_de_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente_id} - {self.servico}"
