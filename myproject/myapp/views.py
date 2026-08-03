from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 200:
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        age = request.POST.get("age")

    return render(request, 'cadastro.html')