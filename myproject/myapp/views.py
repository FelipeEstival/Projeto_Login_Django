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
        name_digitado = request.POST.get("name")
        email_digitado = request.POST.get("email")
        password_digitado = request.POST.get("password")
        age_digitado = request.POST.get("age")

        context = {
            "name": name_digitado,
            "email": email_digitado,
            "password": password_digitado,
            "age": age_digitado
        } 

        Usuario = Person(
            name = name_digitado, email = email_digitado, password = password_digitado, age = age_digitado
        )
        Usuario.save()

        return render(request, 'cadastro.html', context)

    return render(request, 'cadastro.html')