from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario


def home(request):
    if request.method == "POST":
        # Process the form data
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")
        user = Usuario(nome=nome, email=email)
        user.save()
        return HttpResponse("Form submitted successfully by " + nome + "!")
    else:
        return render(request, 'landpage.html')

# Create your views here.
