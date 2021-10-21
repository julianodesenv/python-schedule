from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    user = request.POST.get('user')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=user, password=password)
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso!')
        return redirect('dashboard')
    

def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')
    
    error = False
    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    user = request.POST.get('user')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_confirm = request.POST.get('password_confirm')

    if not name or not last_name or not user or not email or not password or not password_confirm:
        error = True
        messages.error(request, 'Todos os campos são obrigatórios.')

    try:
        validate_email(email)
    except:
        error = True
        messages.error(request, 'E-mail inválido.')

    if len(password) < 6:
        error = True
        messages.error(request, 'Senha precisa de no minimo 6 caracteres.')

    if password != password_confirm:
        error = True
        messages.error(request, 'Senhas não conferem.')

    if User.objects.filter(username=user).exists():
        error = True
        messages.error(request, 'Usuário já existe.')

    if User.objects.filter(email=email).exists():
        error = True
        messages.error(request, 'E-mail já existe.')

    if error:
        return render(request, 'accounts/register.html')

    user = User.objects.create_user(username=user, email=email, password=password, first_name=name, last_name=last_name)
    user.save()

    messages.success(request, 'Registrado com sucesso! Utilize os campos abaixo para entrar.')
    return redirect('login')
    
    
@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')