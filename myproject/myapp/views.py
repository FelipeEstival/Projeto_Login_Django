from django.shortcuts import render
from django.contrib import messages
from .models import Person

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    Usuario = Person()

    if request.method == "POST":
        name_digitado = request.POST.get("name").strip()
        email_digitado = request.POST.get("email").strip().lower()
        password_digitado = request.POST.get("password")
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

        try:
            Usuario = Person(
                name = name_digitado, email = email_digitado, password = password_digitado, age = age_digitado
            )
            Usuario.save()
        except: 
            messages.error(request, "Erro, não foi possível cadastrar.")
            return render(request, "cadastro.html", context)

        messages.success(request, "Cadastrado com sucesso!")

        return render(request, 'cadastro.html', context)

    return render(request, 'cadastro.html')