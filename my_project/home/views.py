from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .models import Administrador



def messages_view(request):
    mensagens = Usuario.objects.all().order_by("-criado_em")
    return render(request, 'messages_list.html', {
        "mensagens": mensagens
    })


def login_view(request):
    if request.method == "POST":
        # Process the form data
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        admin = Administrador.objects.filter(email=email, senha=senha)
    

        if admin.exists():
            return render(request, 'messages_list.html')
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
