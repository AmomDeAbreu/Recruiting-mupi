from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import render

def login_view(request):
    if request.method == "POST":
        # Process the form data
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        user = Usuario.objects.filter(nome=nome, senha=senha)
        if user.exists():
            return HttpResponse("Login successful for " + nome + "!")
        else:
            return HttpResponse("Invalid username or password!")
    else:
        return render(request, 'login.html')


def home(request):
    if request.method == "POST":
        # Process the form data
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")
        user = Usuario(nome=nome, email=email, mensagem=mensagem)
        user.save()
        return HttpResponse("Form submitted successfully by " + nome + "!")
    else:
        return render(request, 'landpage.html')



# Create your views here.
