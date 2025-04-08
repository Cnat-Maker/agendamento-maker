from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import Usuario

class LoginView(View):
    def get(self, request):
        return render(request, 'usuarios/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'usuarios/login.html', {'error': 'Usuário ou senha inválidos'})

class CadastroView(View):
    def get(self, request):
        return render(request, 'usuarios/cadastro.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']

        user = Usuario.objects.create_user(
            username=username,
            password=password,
            email=email,
            cpf=cpf,
            telefone=telefone
        )
        user.save()
        return redirect('agendamento')
