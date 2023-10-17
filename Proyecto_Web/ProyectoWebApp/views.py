from django.shortcuts import render, HttpResponse
from carro.carro import Carro
# Create your views here.

def home(request):
    
    carro = Carro(request)
    return render(request, "ProyectoWebApp/home.html")



"""creamos carro aqui al principio porque da problemas si no haces los cambios que hice yo para que 
 siempre se viera el carro estes logueado o no"""
