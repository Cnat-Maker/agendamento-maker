from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Agendamento, Servico

class AgendamentoView(View):
    def get(self, request):
        servicos = Servico.objects.all()

        contexto = {
            'servicos': servicos,
        }

        return render(request, 'agendamentos/agendamento.html', contexto) 

    def post(self, request):
        servico_id = request.POST.get('servico')
        servico = get_object_or_404(Servico, id=servico_id)

        data_prevista = request.POST.get('data_prevista')
        motivo = request.POST.get('motivo')

        # Cria o agendamento com os dados do formulário
        agendamento = Agendamento(
            servico=servico,
            cliente=request.user,
            data_prevista=data_prevista,
            motivo=motivo,
        )

        # Salvando o agendamento
        agendamento.save()
        
        # Redirecionar ou renderizar uma resposta
        return redirect('agendamento')  # Ajuste conforme necessário
