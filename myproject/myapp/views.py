from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Person
from django.contrib.auth.hashers import make_password, check_password
from .validar import validar_senha

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    email_digitado = request.POST.get("email")
    password_digitado = request.POST.get("password")

    usuario = Person.objects.filter(email = email_digitado).first()
    if usuario:
        if check_password(password_digitado, usuario.password): 
            request.session["usuario_id"] = usuario.id
            return redirect('screen')
        else:
            messages.error(request, "Senha incorreta, tente novamente")

    return render(request, 'login.html')

def cadastro(request):
    Usuario = Person()

    if request.method == "POST":
        name_digitado = request.POST.get("name").strip()
        email_digitado = request.POST.get("email").strip().lower()
        password_digitado = request.POST.get("password").strip()
        age_digitado = request.POST.get("age")

        context = {
            "name": name_digitado,
            "email": email_digitado,
            "password": password_digitado,
            "age": age_digitado
        } 

        if len(name_digitado) < 3:
            messages.error(request, "Insira um nome válido.")
            return render(request, "cadastro.html", context)
                
        if not name_digitado.replace(" ", "").isalpha():
            messages.error(request, "Insira um nome válido.")
            return render(request, "cadastro.html", context)
                
        if not age_digitado.isdigit():
            messages.error(request, "Insira uma idade válida.")
            return render(request, "cadastro.html", context)
        
        age_num = int(age_digitado)
        if age_num < 18 or age_num > 120:
            messages.error(request, "Insira uma idade válida.")
            return render(request, "cadastro.html", context)

        password_validacao = validar_senha(password_digitado)
        if password_validacao != "sucesso":
             messages.error(request, password_validacao)
             return render(request, "cadastro.html", context)

        try:
            Usuario = Person(
                name = name_digitado, email = email_digitado, password = make_password(password_digitado), age = age_digitado
            )
            Usuario.save()
        except: 
            messages.error(request, "Erro, não foi possível cadastrar.")
            return render(request, "cadastro.html", context)

        messages.success(request, "Cadastrado com sucesso!")

        return render(request, 'cadastro.html', context)

    return render(request, 'cadastro.html')

def screen(request):
    usuario_id = request.session.get("usuario_id")
    usuario = Person.objects.get(id=usuario_id)

    return render(request, "screen.html", {
        "usuario": usuario
    })

def logout(request):
    request.session.flush()
    return redirect("login")

def esqueci_minha_senha(request):
    email_digitado = request.POST.get("email")
    usuario = Person.objects.filter(email = email_digitado).first()

    if request.method == "POST":
        if usuario: 
                request.session["usuario_id"] = usuario.id
                return redirect('recriar_senha')
        else:
            messages.error(request, "Email não encontrado, tente novamente")
            return render(request, 'esqueci_senha.html')

    return render(request, 'esqueci_senha.html')
    
def recriar_senha(request):
    usuario_id = request.session.get("usuario_id")
    usuario = Person.objects.filter(id=usuario_id).first()

    if usuario:
        if request.method == "POST":
                nova_senha = request.POST.get("nova_senha")
                confirmar_senha = request.POST.get("confirmar_senha")

                if nova_senha == confirmar_senha:
                        usuario.password = make_password(nova_senha)
                        usuario.save()
                        messages.success(request, "Senha cadastrada com sucesso.")
                else:
                    messages.error(request, "Senha não compatível")
                    
    return render(request, 'recriar_senha.html')