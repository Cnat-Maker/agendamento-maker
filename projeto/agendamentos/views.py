from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Agendamento

class AgendamentoView(View):
    def get(self, request):
        return render(request, 'agendamentos/agendamento.html') 