# agendamentos/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('agendamento/', AgendamentoView.as_view(), name='agendamento')
]
