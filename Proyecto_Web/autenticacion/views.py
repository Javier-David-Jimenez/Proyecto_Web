from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class Vregistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})
    
    #importamos el usercreationform para hacer el formulario de usuario
    
    def post(self, request):
        pass
    