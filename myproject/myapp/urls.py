from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('screen/', views.screen, name="screen"),
    path('logout/', views.logout, name="logout"),
    path('esqueci_minha_senha/', views.esqueci_minha_senha, name = "esqueci_senha"),
    path('recriar_senha/', views.recriar_senha, name = "recriar_senha"),

]